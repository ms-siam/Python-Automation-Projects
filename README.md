# 🐍 Python Automation Projects

Welcome to my collection of small automation projects I built while learning Python!

Each folder/script here focuses on automating a simple, real-world task — from backing up files and sending emails to working with regex, the clipboard, or the browser. Most of these were inspired by the book **"Automate the Boring Stuff with Python"** and then slightly customized or extended as I experimented with the code.

---

## 📁 Projects Overview

| Project Name | Description |
|--------------|-------------|
| **BackingUptoZip** | Zips up an entire folder and names the zip file with an incremental number. |
| **CommandLineEmailer** | Opens Gmail and prepares an email from the command line interface. |
| **DelUnneededFiles** | Walks through folders to find and (optionally) delete files that are too large. |
| **ProjectDownloadAllXKCDComics** | Downloads all XKCD comics using requests and BeautifulSoup. |
| **ProjectOpeningAllSearch** | Opens multiple search result tabs in the browser using webbrowser module. |
| **ProjectmapItpyWithThewebbrowserModule** | Opens Google Maps in the browser for a given address. |
| **RandomQuizGenerator** | Generates multiple-choice quizzes and answer keys using Python and randomization. |
| **RegexSearch** | Searches for regex patterns inside multiple files and lists matched lines. |
| **RenamingFilesWithDate** | Renames files from one date format to another (e.g., US to EU style). |
| **SelectiveCopy** | Copies only specific file types from one folder to another. |
| **UpdateableMultiClipboard** | Clipboard program with save, load, and now **delete** functionality for saved items. |

---

## 🧠 What I Learned

- File handling with `os`, `shutil`, `zipfile`
- Working with `webbrowser`, `requests`, `bs4`
- Regex with `re` module
- Automating email and browser tasks
- Basic CLI interfaces
- JSON and persistence
- Looping, error handling, and building small reusable scripts

---

## 📅 Project Timeline

This project was built between **February 1 and February 13, 2025**, during my early Python learning phase. Some scripts include comments or code toggles for testing purposes (e.g., skipping deletions or file renaming during test runs).

---

## 📌 Notes

- Most scripts are safe to run, but **always review the code before executing**, especially those related to file deletion or renaming.
- A few scripts are commented for test-mode or debugging.

---

## 🔧 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/ms-siam/Python-Automation-Projects.git
   cd Python-Automation-Projects
   ```

2. Run any script using:
   ```bash
   python3 script_name.py
   ```

> ⚠️ Make sure you have the required modules installed (`requests`, `bs4`, etc.) for some projects.

---

## 🙌 Final Thoughts

These projects were part of my early Python learning journey. I created, tweaked, and documented them as I went along — not for production use but for **building hands-on experience**.