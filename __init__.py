from aqt import mw, gui_hooks

def auto_enable_auto_advance():
    """Automatically enable auto advance when reviewing"""
    if mw.state != "review" or not mw.reviewer:
        return
    
    reviewer = mw.reviewer
    if hasattr(reviewer, 'auto_advance_enabled') and not reviewer.auto_advance_enabled:
        if hasattr(reviewer, 'toggle_auto_advance'):
            reviewer.toggle_auto_advance()
        else:
            reviewer.auto_advance_enabled = True

def on_reviewer_did_show_question(card):
    """Hook that runs when a question is shown"""
    auto_enable_auto_advance()

gui_hooks.reviewer_did_show_question.append(on_reviewer_did_show_question)
