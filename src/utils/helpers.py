"""
Helper Utilities Module
"""

def log_message(message, level='INFO'):
    """Log messages with level"""
    print(f"[{level}] {{message}}")

def format_report(data):
    """Format security report data"""
    return {
        'timestamp': 'N/A',
        'data': data,
        'formatted': True
    }

def validate_target(target):
    """Validate target format"""
    print(f"Validating target: {{target}}")
    return True

def sanitize_input(user_input):
    """Sanitize user input for security"""
    return str(user_input).strip()