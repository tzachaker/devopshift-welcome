import os
import sys
import logging
import json

class JasonFormater(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log = {
            "time": record.created,  
            "module": record.module,  
            "level": record.levelname,  
            "message": record.getMessage() 
        }
        return json.dumps(log)  

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def check_service_status(server_name):
    servers = ["nginx", "docker"]
    
    if server_name in servers:
        logging.info(f"Server '{server_name}' is running")  
        return "Running"
    else:
        raise ValueError(f"Server '{server_name}' is not in the list of servers")

def main():

    # while True:
        try:
            server_name = input("Enter the server name to check status: ") 
            status = check_service_status(server_name)
            print(f"The status of server '{server_name}'is: {status}")
    
        except ValueError as e:
            logging.error(f"Error: {e}")
            print(f"Error: {e}")
        logger = logging.getLogger("myapp")
        logger.setLevel(logging.DEBUG) 
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(JasonFormater())
        logger.addHandler(handler)
        logger.info("This is an info message.")
        logger.error("This is an error message.")
        logger.debug("This is an debug message.")
    

if __name__ == "__main__":
    main()

