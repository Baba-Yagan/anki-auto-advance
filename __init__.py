from aqt import mw, gui_hooks

# Track if we've already enabled auto-advance for this session
_auto_advance_enabled_this_session = False

def auto_enable_auto_advance():
    """Automatically enable auto advance when reviewing"""
    global _auto_advance_enabled_this_session
    
    if mw.state != "review" or not mw.reviewer:
        return
    
    # Only try to enable once per session
    if _auto_advance_enabled_this_session:
        return
    
    reviewer = mw.reviewer
    if hasattr(reviewer, 'auto_advance_enabled') and not reviewer.auto_advance_enabled:
        if hasattr(reviewer, 'toggle_auto_advance'):
            reviewer.toggle_auto_advance()
            _auto_advance_enabled_this_session = True

def on_reviewer_did_show_question(card):
    """Hook that runs when a question is shown"""
    auto_enable_auto_advance()

def on_reviewer_did_init(reviewer):
    """Reset session flag when reviewer is reinitialized"""
    global _auto_advance_enabled_this_session
    _auto_advance_enabled_this_session = False

gui_hooks.reviewer_did_show_question.append(on_reviewer_did_show_question)
gui_hooks.reviewer_did_init.append(on_reviewer_did_init)
