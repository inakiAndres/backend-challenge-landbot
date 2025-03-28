# **Run It: Setting Up Django API with Docker**

This guide will help you to run the project with Docker. 

---

## **Prerequisites**

Before you start, make sure you have the following installed on your local machine:

- **Docker**: [Install Docker](https://www.docker.com/get-started)
- **Docker Compose**: It is included with Docker Desktop, so no separate installation is needed.

---

## **Setup Instructions**

### **1. Clone the Repository**


```bash
git clone https://github.com/inakiAndres/backend-challenge-lanbot.git
```

### **2. Configure Environment Variables**
For local development, we use a `.env` file to manage environment variables securely.

Create a `.env` file in the root of your project and add the `SECRET_KEY`. Example:

```
SECRET_KEY=your-secure-secret-key-here
```

### **3. Build and Run with Docker Compose**


#### 1. Build the Docker image:
Run:
```
docker-compose up --build
```
This will make the app available at http://localhost:8001 


You can stop the services by running:

```
docker-compose down
```

### **4. Running Tests**


```
docker-compose run web python manage.py test
```

This will execute the tests inside the Docker container, ensuring that everything is working correctly.

## **Directory Structure**
Here is a quick overview of the project structure:

TBD

## **Troubleshooting**
### **1. "Port already in use" Error**
If you encounter an error about the port being already in use (e.g., Port 8001 is already allocated), make sure the port is free. You can either stop the service running or modify the port in the `dockerfile` or `docker-compose.yml` command.

### **2. Missing `.env` File**
Ensure you’ve created a `.env` file in the root directory, as it’s required for the environment variables, including `SECRET_KEY`. If the file is missing, Django might fail to start.