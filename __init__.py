from aqt import mw
from aqt.utils import showInfo
from anki.hooks import addHook
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def auto_enable_auto_advance():
    """Automatically enable auto advance when reviewing"""
    logger.info("auto_enable_auto_advance() called")
    if mw.state == "review":
        logger.info("In review state, attempting to enable auto advance")
        # Enable auto advance in the reviewer
        if hasattr(mw.reviewer, 'auto_advance'):
            mw.reviewer.auto_advance = True
            logger.info("Set mw.reviewer.auto_advance = True")
        else:
            logger.info("mw.reviewer does not have auto_advance attribute")
        # Also set the config if available
        config = mw.addonManager.getConfig(__name__)
        if config:
            config['auto_advance_enabled'] = True
            mw.addonManager.writeConfig(__name__, config)
            logger.info("Updated addon config")
    else:
        logger.info(f"Not in review state, current state: {mw.state}")

def on_reviewer_did_show_question():
    """Hook that runs when a question is shown"""
    logger.info("on_reviewer_did_show_question() triggered")
    auto_enable_auto_advance()

def on_reviewer_did_show_answer():
    """Hook that runs when an answer is shown"""
    logger.info("on_reviewer_did_show_answer() triggered")
    auto_enable_auto_advance()

# Add hooks to enable auto advance
addHook("reviewerDidShowQuestion", on_reviewer_did_show_question)
addHook("reviewerDidShowAnswer", on_reviewer_did_show_answer)

# Also try to enable it when the addon loads
logger.info("Auto Advance Enabler addon loaded")
auto_enable_auto_advance()
