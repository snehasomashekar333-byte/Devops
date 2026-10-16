# Exercise 5: Docker Security with AppArmor
## Aim
To understand how AppArmor can be used to restrict application actions and improve container security.
## Tools Used
- Docker
- AppArmor
- Python
## Overview
AppArmor is a Linux security module that can restrict the actions a program is allowed to perform. When used with containers, security profiles can help limit application capabilities and reduce potential risks.
## Files
- `app.py` - Application code
- `Dockerfile` - Instructions for building the Docker image
- `apply_apparmor.py` - Script related to applying the AppArmor configuration
- `test_restricted_actions.py` - Tests for restricted actions
- `outputs/` - Saved command outputs and logs
- `screenshots/` - Exercise screenshots
## Procedure
1. Review the application code and Dockerfile.
2. Review the AppArmor-related script and security configuration.
3. Build and run the container as required by the exercise.
4. Run the tests for restricted actions.
5. Review the outputs and screenshots.
## Result
This exercise demonstrates the role of AppArmor in restricting application behavior and improving Docker container security.
