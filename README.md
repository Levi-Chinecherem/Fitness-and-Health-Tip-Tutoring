
# Computerized Fitness and Health Tip Tutoring Information Management System

The Computerized Fitness and Health Tip Tutoring Information Management System is a web application built using Django that allows users to access fitness and health tips, manage their user profiles, and perform CRUD operations on fitness tips. This README provides an overview of the project and instructions for setting it up and using it.

## Features

- User Authentication: Users can register, log in, log out, and reset their passwords.
- User Profiles: Users can create, view, update, and delete their profiles.
- Fitness Tips: Users can create, view, update, and delete fitness tips.
- Rich Text Content: Fitness tips support rich text content with images, thanks to CKEditor.
- User Permissions: Users can only perform CRUD operations on their own fitness tips and profiles.

## Project Structure

The project consists of two Django apps: "fitness_app" and "accounts." Here's a brief overview of their functionalities:

- `fitness_app`: Manages fitness tips and user profiles.
- `accounts`: Handles user authentication and provides custom templates for authentication views.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- CKEditor
- Bootstrap 4
- Internet connection to load CKEditor and Bootstrap 4 CSS and JS files

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd fitness-health-tip-management-system
   ```
2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```
3. Migrate the database:

   ```bash
   python manage.py migrate
   ```
4. Create a superuser account:

   ```bash
   python manage.py createsuperuser
   ```
5. Run the development server:

   ```bash
   python manage.py runserver
   ```
6. Access the application in your web browser at `http://localhost:8000`.

## Usage

- Log in using your superuser account or register a new user account.
- Create and manage your user profile.
- Create, update, and delete fitness tips.
- View fitness tips and profiles.

## Screenshots

Here are some sample screenshots of the application:

![Screenshot 1](sample-screenshots/screenshot1.png)

![Screenshot 2](sample-screenshots/screenshot2.png)

![Screenshot 3](sample-screenshots/screenshot3.png)

## Contributing

Feel free to contribute to the project by opening issues or creating pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thank you to the Django, CKEditor, and Bootstrap communities for their excellent tools and resources.

## Author

[Levi Chinecherem C.]

---
