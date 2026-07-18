# GitHub User Analyzer

A Python command-line application that analyzes GitHub users using the GitHub REST API. The application fetches user information, analyzes repositories, and displays useful statistics in a clean and organized format.

## Features

* Fetch GitHub user profile information
* Display:

  * Name
  * Username
  * Bio
  * Public repositories
  * Followers
  * Following
  * Account creation date
  * Location
  * Company
* Retrieve all public repositories
* Display the top 3 repositories based on stars
* Calculate repository statistics:

  * Total repositories
  * Total stars
  * Average stars per repository
  * Most used programming language
* Filter repositories by programming language (case-insensitive)
* Handle missing profile information gracefully
* Handle invalid usernames and GitHub API errors
* Authenticate requests using a GitHub Personal Access Token (PAT)

---

## Technologies Used

* Python 3
* Requests
* python-dotenv
* GitHub REST API

---

## Project Structure

```text
GitHub User Analyzer/
│
├── analyzer.py        # Repository analysis and statistics
├── github_api.py      # GitHub API communication
├── ui.py              # User interface and output
├── main.py            # Application entry point
├── requirements.txt
├── .gitignore
├── .env               # Not committed to Git
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Naqeeb06/github_user_analyzer.git
```

Navigate into the project:

```bash
cd github_user_analyzer
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root:

```env
GITHUB_TOKEN=your_personal_access_token
```

The token is required to authenticate GitHub API requests and avoid the low unauthenticated rate limit.

---

## Running the Project

```bash
python main.py
```

Enter a GitHub username when prompted.

Example:

```text
Enter the GitHub username you want to analyze: octocat
```

---

## Example Features

* View GitHub user profile
* Display top repositories by stars
* Repository statistics
* Filter repositories by programming language

---

## Error Handling

The application handles:

* Invalid GitHub usernames
* API rate limiting
* Authentication issues
* Missing profile information
* Repositories without a specified language

---

## Future Improvements

* Interactive menu-driven interface
* Better date formatting
* Improved number formatting
* Repository sorting by additional metrics
* Export results to CSV or JSON
* Unit tests

---

## Author

**Naqeeb**

Computer Science Student | Aspiring AI Engineer
