# NewsApp

NewsApp is a Flask-based web application that fetches and displays the latest news articles based on different categories such as Business, Technology, and Sports. The app uses the NewsAPI to retrieve news articles and features a simple web interface to browse through different categories.

## Features
- Fetches news articles dynamically from NewsAPI.
- Categorized news sections (Business, Technology, Sports, and General).
- Uses Flask for backend development.
- Implements Swagger API documentation.
- Saves API responses to JSON files for easy access and debugging.

## Technologies Used
- Flask
- Requests (for API calls)
- Flasgger (for API documentation)
- HTML & Jinja2 Templates (for rendering news articles)

## Installation
### Prerequisites
- Python 3.x installed
- Virtual environment (optional but recommended)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/NewsApp.git
   cd NewsApp
   ```
2. Create a virtual environment (optional):
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up NewsAPI key:
   - Sign up at [NewsAPI](https://newsapi.org/) and get an API key.
   - Update `app.py` with your API key:
     ```python
     API_KEY = "your_api_key_here"
     ```

## Running the Application
```sh
python app.py
```
The application will be accessible at `http://127.0.0.1:5000/`.

## API Endpoints
| Endpoint | Description |
|----------|-------------|
| `/` | Fetches general news (default: Tesla) |
| `/business` | Fetches Business news |
| `/technology` | Fetches Technology news |
| `/sports` | Fetches Sports news |

## Swagger API Documentation
Swagger is integrated for API documentation.
- After running the app, visit `http://127.0.0.1:5000/apidocs/` to view API documentation.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to fork this repository, open issues, and submit pull requests to improve the application!

