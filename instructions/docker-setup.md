# Docker Desktop Setup Guide

Quick guide to installing Docker Desktop on Windows and Mac for the AI Upskills Workshop.

## Prerequisites

- **Windows**: Windows 10 64-bit or later (Pro, Enterprise, or Education) with WSL 2 feature enabled
- **Mac**: macOS 10.15 or later (Apple Silicon or Intel chip)

## Installation

### Windows

1. **Download**: [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
2. **Run the installer** and follow the on-screen instructions
3. **Permissions**: Administrator privileges required during installation. See [Requesting Temporary Admin](https://disney.service-now.com/dtoolsitsp?id=kb_article&sys_id=d3efd8bb9330ee50e25b32aa6aba10e9) from DToolsIT.

### Mac

1. **Download**: [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)
   - Choose the correct version for your chip (Apple Silicon or Intel)
2. **Install**: Open the downloaded `.dmg` file and drag Docker to Applications folder
3. **Permissions**: You may be prompted to grant permissions for:
   - Installing symlinks in `/usr/local/bin`
   - Binding to privileged ports
   - Modifying `/etc/hosts`

- See [Requesting Temporary Admin](https://disney.service-now.com/dtoolsitsp?id=kb_article_viewer&sysparm_article=KB0073873&sys_kb_id=a8c7bc1e4799e59096884497436d4346) from DToolsIT

## First Launch

1. **Open Docker Desktop** from:
   - **Windows**: Start menu or Desktop shortcut
   - **Mac**: Applications folder

2. **Accept the Docker Subscription Service Agreement** when prompted

3. **Wait for Docker to start** - You'll see the Docker icon in:
   - **Windows**: System tray (bottom right)
   - **Mac**: Menu bar (top right)

4. **Verify installation**:
```bash
docker --version
docker-compose --version
```

## Important Considerations

- **First-Time Setup**: Docker Desktop may perform additional setup steps on first launch. Ensure you have a stable internet connection.

- **Windows Users**: If you're not added to the `docker-users` group automatically, you may need to:
  - Open Computer Management as administrator
  - Navigate to Local Users and Groups > Groups > docker-users
  - Add your user account
  - Sign out and back in

- **Running Status**: Docker Desktop runs in the background. Check the system tray/menu bar icon to verify it's running.

## Troubleshooting

- **Docker won't start**: Check system requirements and ensure virtualization is enabled in BIOS (Windows)
- **Permission errors**: Ensure you're in the `docker-users` group (Windows) or granted necessary permissions (Mac)
- **Network issues**: Verify internet connection for first-time setup

## Getting Help

- [Docker Desktop Documentation](https://docs.docker.com/desktop/)
- [Docker Desktop FAQs](https://docs.docker.com/desktop/faqs/)
- Contact workshop instructors for assistance

---

*This guide is part of Disney's AI Engineering Workshop materials.*

