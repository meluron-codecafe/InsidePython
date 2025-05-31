from IPython.display import HTML

def tutbox(content, box_type="note", title=None):
    """
    Generate a beautiful tutorial information box for Jupyter notebooks.
    
    Parameters:
    -----------
    content : str
        The main content/message to display in the box
    box_type : str, optional
        Type of box to create. Options: 'note', 'tip', 'warning', 'danger', 
        'important', 'example', 'exercise', 'success', 'info', 'code'
        Default: 'note'
    title : str, optional
        Custom title for the box. If None, uses the default title for the box type
    
    Returns:
    --------
    IPython.display.HTML
        HTML object that renders the tutorial box
    
    Example:
    --------
    tutbox("This is a helpful tip!", "tip")
    tutbox("Be careful with this operation", "warning", "Custom Warning")
    """
    
    # Box configurations: (icon, color, bg_color, border_color, default_title)
    box_configs = {
        'note': ('📝', '#0d47a1', '#e3f2fd', '#2196f3', 'Note'),
        'tip': ('💡', '#1b5e20', '#e8f5e8', '#4caf50', 'Tip'),
        'question': ('❓', '#6a1b9a', '#f3e5f5', '#9c27b0', 'Question'),
        'warning': ('⚠️', '#e65100', '#fff3e0', '#ff9800', 'Warning'),
        'danger': ('🚨', '#b71c1c', '#ffebee', '#f44336', 'Danger'),
        'important': ('⭐', '#4a148c', '#f3e5f5', '#9c27b0', 'Important'),
        'example': ('📋', '#004d40', '#e0f2f1', '#009688', 'Example'),
        'exercise': ('🏋️', '#1a237e', '#e8eaf6', '#3f51b5', 'Exercise'),
        'success': ('✅', '#33691e', '#f1f8e9', '#8bc34a', 'Success'),
        'info': ('ℹ️', '#006064', '#e0f7fa', '#00bcd4', 'Info'),
        'code': ('💻', '#263238', '#f5f5f5', '#607d8b', 'Code'),
        'upcoming': ('🔜', '#1565c0', '#e3f2fd', '#42a5f5', 'Coming Up Next')
    }
    
    # Validate box_type
    if box_type not in box_configs:
        available_types = ', '.join(box_configs.keys())
        raise ValueError(f"Invalid box_type '{box_type}'. Available types: {available_types}")
    
    # Get configuration for the specified box type
    icon, text_color, bg_color, border_color, default_title = box_configs[box_type]
    
    # Use provided title or default
    display_title = title if title is not None else default_title
    
    # Generate HTML
    html_content = f"""
    <div style="
        margin: 15px 0; 
        padding: 16px 20px; 
        border-radius: 8px; 
        border-left: 4px solid {border_color}; 
        display: flex; 
        align-items: flex-start; 
        gap: 12px; 
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); 
        background-color: {bg_color}; 
        color: {text_color};
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    ">
        <div style="
            font-size: 20px; 
            margin-top: 2px; 
            flex-shrink: 0;
        ">{icon}</div>
        <div style="flex: 1;">
            <div style="
                font-weight: bold; 
                margin-bottom: 6px; 
                font-size: 14px; 
                text-transform: uppercase; 
                letter-spacing: 0.5px;
            ">{display_title}</div>
            <div style="
                margin: 0; 
                font-size: 14px; 
                line-height: 1.5;
            ">{content}</div>
        </div>
    </div>
    """
    
    return HTML(html_content)


# Convenience functions for each box type
def note(content, title=None):
    """Create a note box"""
    return tutbox(content, "note", title)

def tip(content, title=None):
    """Create a tip box"""
    return tutbox(content, "tip", title)

def warning(content, title=None):
    """Create a warning box"""
    return tutbox(content, "warning", title)

def danger(content, title=None):
    """Create a danger box"""
    return tutbox(content, "danger", title)

def important(content, title=None):
    """Create an important box"""
    return tutbox(content, "important", title)

def example(content, title=None):
    """Create an example box"""
    return tutbox(content, "example", title)

def exercise(content, title=None):
    """Create an exercise box"""
    return tutbox(content, "exercise", title)

def success(content, title=None):
    """Create a success box"""
    return tutbox(content, "success", title)

def info(content, title=None):
    """Create an info box"""
    return tutbox(content, "info", title)

def code_box(content, title=None):
    """Create a code explanation box"""
    return tutbox(content, "code", title)

def question(content, title=None):
    """Create a question box"""
    return tutbox(content, "question", title)

def upcoming(content, title=None):
    """Create an upcoming/next section box"""
    return tutbox(content, "upcoming", title)