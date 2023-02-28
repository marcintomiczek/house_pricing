### To fill in database
`python -m house_pricing.cli init-db`

### To run the application
`python -m uvicorn house_pricing.main:app`

Remember to set env variables:
- DB_PROVIDER
- DB_URL
- USER
- PASSWORD
