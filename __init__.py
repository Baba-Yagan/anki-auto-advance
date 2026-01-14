from aqt import mw, gui_hooks

def auto_enable_auto_advance(reviewer=None):
    """Automatically enable auto advance when reviewing"""
    try:
        # If reviewer is passed as argument, use it; otherwise use mw.reviewer
        target_reviewer = reviewer if reviewer else mw.reviewer
        
        if not target_reviewer:
            return
        
        if mw.state == "review" or reviewer:
            # Enable auto advance using the correct attribute
            if hasattr(target_reviewer, 'auto_advance_enabled'):
                if not target_reviewer.auto_advance_enabled:
                    # Use toggle_auto_advance to enable it
                    if hasattr(target_reviewer, 'toggle_auto_advance'):
                        target_reviewer.toggle_auto_advance()
                    else:
                        # Fallback to setting the attribute directly
                        target_reviewer.auto_advance_enabled = True
            
            # Also set the config if available
            try:
                config = mw.addonManager.getConfig(__name__)
                if config:
                    config['auto_advance_enabled'] = True
                    mw.addonManager.writeConfig(__name__, config)
            except:
                pass  # Silently ignore config errors
    except:
        pass  # Silently ignore all errors to prevent I/O issues

def on_reviewer_did_init(reviewer):
    """Hook that runs when reviewer is initialized"""
    try:
        auto_enable_auto_advance(reviewer)
    except:
        pass

def on_reviewer_did_show_question(card):
    """Hook that runs when a question is shown"""
    try:
        auto_enable_auto_advance()
    except:
        pass

# Use new style hooks
try:
    gui_hooks.reviewer_did_init.append(on_reviewer_did_init)
    gui_hooks.reviewer_did_show_question.append(on_reviewer_did_show_question)
except:
    pass

# Also try to enable it when the addon loads
try:
    auto_enable_auto_advance()
except:
    pass
