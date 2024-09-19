import os

# Ensure DATABASE_URL can be fetched from environment variables
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://sit722_part3_db_user:gS4ZrYN42FYsXTyfTnaHpELURuhXNcDb@dpg-crm4hgij1k6c73fjgb1g-a.oregon-postgres.render.com/sit722_part3_db?sslmode=require')
