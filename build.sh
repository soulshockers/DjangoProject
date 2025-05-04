#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
python manage.py migrate

# Conditionally create superuser using environment variables
echo "Checking if superuser exists..."
SUPERUSER_EXISTS=$(python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
print(User.objects.filter(username='${DJANGO_SUPERUSER_USERNAME}').exists())
")

if [ "$SUPERUSER_EXISTS" = "False" ]; then
  echo "Superuser does not exist, creating..."
  python manage.py createsuperuser --noinput
else
  echo "Superuser '${DJANGO_SUPERUSER_USERNAME}' already exists, skipping creation."
fi