from aqt import mw, gui_hooks
from aqt.utils import showInfo
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def auto_enable_auto_advance(reviewer=None):
    """Automatically enable auto advance when reviewing"""
    logger.info("auto_enable_auto_advance() called")
    
    # If reviewer is passed as argument, use it; otherwise use mw.reviewer
    target_reviewer = reviewer if reviewer else mw.reviewer
    
    if mw.state == "review" or reviewer:
        logger.info("In review state or reviewer provided, attempting to enable auto advance")
        
        # Try different possible attributes for auto advance
        if hasattr(target_reviewer, 'auto_advance'):
            target_reviewer.auto_advance = True
            logger.info("Set reviewer.auto_advance = True")
        elif hasattr(target_reviewer, '_auto_advance'):
            target_reviewer._auto_advance = True
            logger.info("Set reviewer._auto_advance = True")
        else:
            logger.info("Reviewer does not have auto_advance attribute")
            # Log all attributes to see what's available
            attrs = [attr for attr in dir(target_reviewer) if 'advance' in attr.lower()]
            logger.info(f"Available advance-related attributes: {attrs}")
        
        # Also set the config if available
        config = mw.addonManager.getConfig(__name__)
        if config:
            config['auto_advance_enabled'] = True
            mw.addonManager.writeConfig(__name__, config)
            logger.info("Updated addon config")
    else:
        logger.info(f"Not in review state, current state: {mw.state}")

def on_reviewer_did_init(reviewer):
    """Hook that runs when reviewer is initialized"""
    logger.info("on_reviewer_did_init() triggered - reviewer initialized!")
    auto_enable_auto_advance(reviewer)

def on_reviewer_did_show_question(card):
    """Hook that runs when a question is shown"""
    logger.info("on_reviewer_did_show_question() triggered")
    auto_enable_auto_advance()

# Use new style hooks
gui_hooks.reviewer_did_init.append(on_reviewer_did_init)
gui_hooks.reviewer_did_show_question.append(on_reviewer_did_show_question)

# Also try to enable it when the addon loads
logger.info("Auto Advance Enabler addon loaded")
auto_enable_auto_advance()
