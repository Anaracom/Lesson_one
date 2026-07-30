# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: RepairLog
def save_template(template_name, template_data):
    if not template_data:
        raise ValueError("Template data cannot be empty")
    with open('RepairLog/templates.txt', 'a') as f:
        f.write(f"--- Template: {template_name} ---\n")
        for key, value in template_data.items():
            f.write(f"{key}: {value}\n")

def load_templates(template_path='RepairLog/templates.txt'):
    templates = {}
    if not os.path.exists(template_path):
        return templates
    with open(template_path, 'r') as f:
        content = f.read()
    current_name = None
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('--- Template:'):
            current_name = line.replace('--- Template:', '').strip()
        elif current_name and not line.startswith('---'):
            key, value = line.split(': ', 1)
            templates[current_name] = {key.strip(): value.strip()}
    return templates

def create_note_from_template(template_name):
    templates = load_templates()
    if template_name not in templates:
        raise ValueError(f"Template '{template_name}' not found. Available: {', '.join(templates.keys())}")
    items = []
    for key, value in templates[template_name].items():
        user_input = input(f"  Enter {key} [{value}]: ") or value
        items.append((key.strip(), user_input))
    note_data = dict(items)
    if 'title' not in note_data:
        note_data['title'] = template_name
    return note_data

def save_note_from_template(template_name):
    data = create_note_from_template(template_name)
    if 'date' not in data or 'items' not in data:
        raise ValueError("Note must contain 'date' and 'items'.")
    return add_note(data)
