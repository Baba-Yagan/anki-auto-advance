from aqt import mw, gui_hooks

def auto_enable_auto_advance(reviewer=None):
    """Automatically enable auto advance when reviewing"""
    try:
        target_reviewer = reviewer if reviewer else mw.reviewer
        
        if not target_reviewer:
            return
        
        # Only enable if we're actually in review state
        if mw.state == "review":
            if hasattr(target_reviewer, 'auto_advance_enabled'):
                if not target_reviewer.auto_advance_enabled:
                    if hasattr(target_reviewer, 'toggle_auto_advance'):
                        target_reviewer.toggle_auto_advance()
                    else:
                        target_reviewer.auto_advance_enabled = True
    except:
        pass

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

try:
#    gui_hooks.reviewer_did_init.append(on_reviewer_did_init)
    gui_hooks.reviewer_did_show_question.append(on_reviewer_did_show_question)
except:
    pass
