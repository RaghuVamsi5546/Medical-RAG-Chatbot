from flask import Flask, render_template, request, session, redirect, url_for
from app.common.logger import get_logger
from app.components.retriever import create_qa_chain
from app.common.exception import CustomException
from markupsafe import Markup
import os

logger = get_logger(__name__)
app = Flask(__name__)
app.secret_key = os.urandom(24)

def nl2br(value):
    return Markup(value.replace("\n", "<br>\n"))

app.jinja_env.filters["nl2br"] = nl2br

try:
    qa_chain = create_qa_chain()
except CustomException as e:
    logger.error(f"Failed to initialize QA chain: {e}", exc_info=True)
    qa_chain = None

@app.route("/", methods=["GET", "POST"])
def index():
    if qa_chain is None:
        return "QA chain failed to initialize. Check logs and GROQ_API_KEY.", 500

    if "messages" not in session:
        session["messages"] = []

    if request.method == "POST":
        user_input = request.form.get("prompt")
        if user_input:
            messages = session["messages"]
            messages.append({"role": "user", "content": user_input})
            session["messages"] = messages

            try:
                response = qa_chain.invoke({"query": user_input})
                messages.append({"role": "assistant", "content": response['result']})
                session["messages"] = messages
            except Exception as e:
                logger.error(f"Error while invoking QA chain: {e}", exc_info=True)
                error_msg = f"Error: {str(e)}"
                return render_template("index.html", messages=session["messages"], error=error_msg)

        return redirect(url_for("index"))

    return render_template("index.html", messages=session.get("messages", []))

@app.route("/clear")
def clear():
    session.pop("messages", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
