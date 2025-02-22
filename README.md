# STK Endpoint

This project provides an endpoint for making STK (Sim Tool Kit) push requests using the Mpesa API. It is built with Django and Django REST Framework.

## Requirements

- Python 3.13.1
- Django 5.1.5
- Django REST Framework
- python-decouple

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Community-Guardian/Stk-endpoint.git
cd Stk-endpoint
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Mpesa credentials:

```plaintext
MPESA_CONSUMER_KEY=your_consumer_key
MPESA_CONSUMER_SECRET=your_consumer_secret
MPESA_SHORTCODE=your_shortcode
MPESA_EXPRESS_SHORTCODE=your_express_shortcode
MPESA_PASSKEY=your_passkey
MPESA_INITIATOR_USERNAME=your_initiator_username
MPESA_INITIATOR_SECURITY_CREDENTIAL=your_initiator_security_credential
MPESA_ENVIRONMENT=sandbox  # or production
STK_PUSH_CALLBACK_URL=your_callback_url
```

5. Apply the migrations:

```bash
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver
```

## Usage

You can now make STK push requests to the endpoint `/api/v1/make-stk-push/` with the required parameters.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.