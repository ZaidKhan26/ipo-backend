from django.core.management import call_command

def run():
    call_command('migrate')
    print("✅ Migrations applied")
