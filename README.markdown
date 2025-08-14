# fast-subcheck

A fast and professional subdomain checker with live CLI output.

## Overview

`fast-subcheck` is a Python-based tool designed to efficiently check subdomains for their availability and status, providing real-time progress updates in the terminal. It supports concurrent requests, is fully configurable, and saves results to an output file. The tool is compatible with Windows, Linux, and macOS, offering a clean and professional CLI interface.

## Features

- **Live Progress Updates**: Displays real-time stats in the terminal, including:
  - Total subdomains to test
  - Subdomains tested so far
  - Active subdomains found and saved
  - Inactive or not found subdomains
- **Multi-threaded**: Configurable concurrent requests for faster scanning
- **Output File**: Automatically creates and updates an output file with results
- **Cross-Platform**: Works seamlessly on Windows, Linux, and macOS
- **User-Friendly**: Clean and professional CLI interface

## Requirements

- **Python**: Version 3.8 or higher
- **Dependencies**:
  ```bash
  pip install requests rich
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TahaHatami/fast-subcheck.git
   ```
2. Navigate to the project directory:
   ```bash
   cd fast-subcheck
   ```
3. Install the required Python libraries:
   ```bash
   pip install requests rich
   ```

## Usage

Run the tool with a list of subdomains to check:

```bash
python subcheck.py subdomains.txt
```

- `subdomains.txt`: A text file containing a list of subdomains to scan (one per line).
- The tool will display live progress in the terminal and save active subdomains to an output file.

### Example

```bash
python subcheck.py example_subdomains.txt
```

**Input file (`example_subdomains.txt`)**:
```
sub1.example.com
sub2.example.com
sub3.example.com
```

**Output**:
- Terminal: Live stats on total subdomains, tested, active, and inactive.
- File: A file (e.g., `active_subdomains.txt`) will be created/updated with active subdomains.

## Configuration

You can customize the tool by modifying the following settings (if supported by the script):
- Number of concurrent threads
- Output file name
- Timeout for requests

Check the script's documentation or help command for specific configuration options:
```bash
python subcheck.py --help
```

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For issues, suggestions, or questions, please open an issue on the [GitHub repository](https://github.com/TahaHatami/fast-subcheck).

---

© 2025 TahaHatami