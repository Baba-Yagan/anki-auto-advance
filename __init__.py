from aqt import mw
from aqt.utils import showInfo
from anki.hooks import addHook

def auto_enable_auto_advance():
    """Automatically enable auto advance when reviewing"""
    if mw.state == "review":
        # Enable auto advance in the reviewer
        if hasattr(mw.reviewer, 'auto_advance'):
            mw.reviewer.auto_advance = True
        # Also set the config if available
        config = mw.addonManager.getConfig(__name__)
        if config:
            config['auto_advance_enabled'] = True
            mw.addonManager.writeConfig(__name__, config)

def on_reviewer_did_show_question():
    """Hook that runs when a question is shown"""
    auto_enable_auto_advance()

def on_reviewer_did_show_answer():
    """Hook that runs when an answer is shown"""
    auto_enable_auto_advance()

# Add hooks to enable auto advance
addHook("reviewerDidShowQuestion", on_reviewer_did_show_question)
addHook("reviewerDidShowAnswer", on_reviewer_did_show_answer)

# Also try to enable it when the addon loads
auto_enable_auto_advance()
