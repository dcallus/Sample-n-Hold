# Project 1: Code Quality Checklist

- Testing
  - All code is working! (testing with console.rb or via Chrome is fine)
  - Methods that don’t touch the database are unit tested (specs)
  - Dead code is removed

- Naming
  - Classes have singular names
  - DB tables have plural names
  - Variables have meaningful names
  - Methods have meaningful names.
  - Controllers have plural names (zombies_controller)

- Indentation is correct

- Project Structure
  - Templates are in folders named according to the resource (e.g. views/zombies/index.html)
  - `app.py` requires the blueprints from each of the controllers.

- Restful routes
  - Your controllers adhere to the RESTful routing conventions (where appropriate)
  - You are using the appropriate methods (GET, POST etc) for the appropriate route
  - All routes are reachable - greedy routes (with params) do not block other ones.

- Good separation of concerns
  - Your business logic is handled by the models
  - You view logic is handled by the views (and view logic is minimal - looping, if / else)

- Single Responsibility
  - Models are responsible for the relevant functionality
  - Methods are small

- Database
  - Use ON DELETE CASCADE where appropriate
  - Relationships are enforced with REFERENCES where appropriate
  - Tables are dropped in correct order

- HTML & CSS
  - Use appropriate (semantic) HTML elements - a table is a table, not just a set of divs or p tags
  - Use labels to help with search optimisation / accessibility
  - (Time permitting) - Try and make things Responsive (adjust to viewing device’s characteristics)

- Git repo: Add a README.md file to your git repo. It should be added to the root of your repo and it will be displayed on the repo’s front page like this: https://github.com/matiassingers/awesome-readme.
The README should contain:
  - running instructions for your applications (so other people can clone it and run it)
  - your brief
  - the technologies you used
  - it can also contain screenshots!
