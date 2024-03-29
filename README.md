<a name="readme-top"></a>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/engomardraidi/test_readme">
    <img src="logo.png" alt="Logo">
  </a>

  <h3 align="center">Tech Tailor - Backend</h3>

  <!-- <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p> -->
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#accounts">Accounts</a></li>
        <li><a href="#dashboard">Dashboard</a></li>
        <li><a href="#picker">PC/Laptop/Mobile Picker</a></li>
      </ul>
    </li>
    <!-- <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Welcome to Tech Tailor, your personalized guide to finding the perfect computing device tailored to your needs! Whether you're a professional in the creative industry, a student on a tight budget, or a gaming enthusiast looking for the latest and greatest hardware, Tech Tailor is here to simplify your decision-making process.

How it work:

The Tech Tailor system is an innovative solution designed to assist users in selecting the most suitable computing devices based on their budget and specific needs. This intelligent system leverages both expert systems and neural networks to provide personalized recommendations for PCs, laptops, and mobile devices.

Why you should use it:
* Receive personalized device suggestions based on your budget and field of use, ensuring a perfect match for your specific needs.
* Streamline the device selection process and save time with a user-friendly interface, eliminating the need for extensive research.
* Benefit from an evolving system that learns from your interactions, providing transparent insights into the decision-making process and ensuring up-to-date recommendations
<!-- :smile: -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![django](https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Below you will find instructions on setting up project locally. To get a local copy up and running, follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python -v 3.10.13
* django
  ```sh
  pip install django
  ```
* django rest-framework
  ```sh
  pip install djangorestframework
  pip install markdown       # Markdown support for the browsable API.
  pip install django-filter  # Filtering support
  ```
* Another required packages
  ```sh
  pip install pandas
  pip install numpy
  pip install djangorestframework-simplejwt
  pip install experta
  pip install fuzzywuzzy
  pip install jinja2
  pip install psycopg2-binary
  pip install pyjwt
  pip install scikit-learn
  pip install urllib3
  ```

### Installation

Below you will find instructions to run project.

1. Clone the repo
   ```sh
   git clone https://github.com/engomardraidi/pc_picker_graduation_project.git
   ```
3. Create project database
   ```sh
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
4. Load all data to database
   ```sh
   python3 manage.py load_all_data
   ```
5. Create super admin
   ```sh
   python3 manage.py super_admin # Create super admin in database
   ```
6. Run server
   ```sh
   python3 manage.py runserver
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Below you will find instructions and everything you need to use the APIs.

* Server run on
  ```sh
  http://127.0.0.1:8000/
  ```
### Accounts

1. Login
   * POST method
   * path
     ```sh
     accounts/login/
     ```
   * Body
     ```sh
     {
       "username": string,
       "password": string,
     }
     ```
   * Content-Type
     ```sh
     multipart/form-data # not allowed application/json
     ```
   * Response
     ```sh
     {
       "id": int,
       "username": string,
       "refresh_exp": int, # timestamp of the refresh expiration time
       "access_token": string,
     }

<p align="right">(<a href="#readme-top">back to top</a>)</p>

2. Refresh token
   * POST method
   * path
     ```sh
     accounts/tokens/refresh/
     ```
   * Response
     ```sh
     {} # with status code 200 (ok) or status code 401 (unauthorized) if user not login
     ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

3. Get account information
   * GET method
   * path
     ```sh
     accounts/{user_id}/
     ```
   * Headers
     ```sh
     Authorization: Bearer {access_token}
     ```
   * Response
     ```sh
     {
       "id": int,
       "username": string,
       "first_name": string,
       "last_name": string,
       "email": string,
       "data_joind": string,
     }
     ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

4. Add new admin
   * Permissions: Only super admins are allowed
   * POST method
   * path
     ```sh
     accounts/new/
     ```
   * Body
     ```sh
     {
       "username": string,
       "first_name": string,
       "last_name": string,
       "email": string,
       "password": string,
     }
    * Headers
      ```sh
      Authorization: Bearer {access_token}
      ```
    * Response
      ```sh
      {
        "id": int,
        "username": string,
        "first_name": string,
        "last_name": string,
        "email": string,
        "data_joind": string,
      }

<p align="right">(<a href="#readme-top">back to top</a>)</p>

5. List of all admins
   * Permissions: Only super admins are allowed
   * GET method
   * path
     ```sh
     accounts/list/
     ```
   * Headers
     ```sh
     Authorization: Bearer {access_token}
     ```
   * Response
     ```sh
     [
       {
         "id": int,
         "username": string,
         "first_name": string,
         "last_name": string,
         "email": string,
         "data_joind": string,
       },
       {
         "id": int,
         "username": string,
         "first_name": string,
         "last_name": string,
         "email": string,
         "data_joind": string,
       },
       ...
     ]
     ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

6. Delete admin
   * Permissions: Only super admins are allowed
   * POST method
   * path
     ```sh
     accounts/delete/
     ```
   * Body
     ```sh
     {
       "user_id": int,
     }
   * Headers
     ```sh
     Authorization: Bearer {access_token}
     ```
   * Response
     ```sh
     {} # with status code 204 (no content)
     ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

7. Logout
   * POST method
   * path
     ```sh
     accounts/logout/
     ```
   * Headers
     ```sh
     Authorization: Bearer {access_token}
     ```
   * Response
     ```sh
     {} # with status code 200 (ok)
     ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Dashboard

1. Motherboards
   * GET, POST, PATCH, DELETE methods
   * paths
     ```sh
     dashboard/motherboards/ # GET list of motherboards data or POST new motherboard
     dashboard/motherboards/<int:id>/ # GET, PATCH (update) or DELETE specific motherboard
     dashboard/motherboards/?search=<string:name> # "GET" request
     ```
   * Body
     ```sh
     # When POST new motherboard
     {
       "name": string,
       "memory_max_capacity": int,
       "price": string,
       "ram_slots": int,
       "m2_pci_e_3": int,
       "m2_pci_e_4": int,
       "usb_3_slots": int,
       "usb_3_headers": int,
       "usb_3_type_c": int,
       "vga": int,
       "dvi": int,
       "display_port": int,
       "hdmi": int,
       "pci_e_3": int,
       "pci_e_4": int,
       "external_image": string, # url
       "image": file,
       "form_factor": int, id of form factor
       "socket": int, # id of socket
       "ram_type": int, # id of ram_type
       "chipset": int, # id of chipset
       "producer": int # id of producer
     }
     ```
   * Headers
      ```sh
      Authorization: Bearer {access_token}
      ```
   * Content-Type
     ```sh
     multipart/form-data # allowed application/json when not upload file image
     ```
   * Response
     ```sh
     # list of motherboards data when GET
     # motherboard information when POST a new
     # motherboard with new information when PATCH
     # status code 204 (no content)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

2. CPUs
   * GET, POST, PATCH, DELETE methods
   * paths
     ```sh
     dashboard/cpus/ # GET list of cpus data or POST new cpu
     dashboard/cpus/<int:id>/ # GET, PATCH (update) or DELETE specific cpu
     ```
   * Body
     ```sh
     # When POST new cpu
     {
       "name": string,
       "price": string,
       "base_clock": float,
       "turbo_clock": float,
       "cores": int,
       "threads": int,
       "tdp": int,
       "integrated_graphics": string,
       "external_image": string, # url
       "image": file,
       "socket": int, # id of socket
       "producer": int # id of producer
     }
     ```
   * Headers
      ```sh
      Authorization: Bearer {access_token}
      ```
   * Content-Type
     ```sh
     multipart/form-data # allowed application/json when not upload file image
     ```
   * Response
     ```sh
     # list of cpus data when GET
     # cpu information when POST a new
     # cpu with new information when PATCH
     # status code 204 (no content)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

3. RAMs
   * GET, POST, PATCH, DELETE methods
   * paths
     ```sh
     dashboard/rams/ # GET list of rams data or POST new ram
     dashboard/rams/<int:id>/ # GET, PATCH (update) or DELETE specific ram
     ```
   * Body
     ```sh
     # When POST new ram
     {
       "name": string,
       "price": string,
       "base_clock": float,
       "turbo_clock": float,
       "cores": int,
       "threads": int,
       "tdp": int,
       "integrated_graphics": string,
       "external_image": string, # url
       "image": file,
       "socket": int, # id of socket
       "producer": int # id of producer
     }
     ```
   * Headers
      ```sh
      Authorization: Bearer {access_token}
      ```
   * Content-Type
     ```sh
     multipart/form-data # allowed application/json when not upload file image
     ```
   * Response
     ```sh
     # list of rams data when GET
     # ram information when POST a new
     # ram with new information when PATCH
     # status code 204 (no content)

4. GPUs
   * GET, POST, PATCH, DELETE methods
   * paths
     ```sh
     dashboard/rams/ # GET list of gpus data or POST new gpu
     dashboard/rams/<int:id>/ # GET, PATCH (update) or DELETE specific gpu
     ```
   * Body
     ```sh
     # When POST new gpu
     {
       "name": string,
       "pci_e": int,
       "vram": int,
       "cores": int,
       "price": string,
       "length": float,
       "slots": float,
       "connectors_8pin": int,
       "connectors_6pin": int,
       "hdmi": int,
       "display_port": int,
       "dvi": int,
       "vga": int,
       "boost_clock": int,
       "memory_clock": int,
       "tdp": int,
       "external_image": string, # url
       "image": file,
       "series": int, # id of series
       "producer": int, # id of producer
       "sync": int # id of sync
     }
     ```
   * Headers
      ```sh
      Authorization: Bearer {access_token}
      ```
   * Content-Type
     ```sh
     multipart/form-data # allowed application/json when not upload file image
     ```
   * Response
     ```sh
     # list of gpus data when GET
     # gpu information when POST a new
     # gpu with new information when PATCH
     # status code 204 (no content)

### Picker

1. Pick PC
   * POST method
   * path
     ```sh
     pick-pc/
     ```
   * Body
     ```sh
     {
       "field_id": int,
       "budget": num,
     }
     ```
   * Response
     ```sh
     {
      "num_of_PCs": int,
      "PCs": [
           {
             "perc": num,
             "total_price": num,
             "pc": {
                      "motherboard": {
                      "id": int,
                      "created_at": string,
                      "updated_at": string,
                      "status": bool,
                      "name": string,
                      "memory_max_capacity": int,
                      "price": string,
                      "ram_slots": int,
                      "m2_pci_e_3": int,
                      "m2_pci_e_4": int,
                      "usb_3_slots": int,
                      "usb_3_headers": int,
                      "usb_3_type_c": int,
                      "vga": int,
                      "dvi": int,
                      "display_port": int,
                      "hdmi": int,
                      "pci_e_3": int,
                      "pci_e_4": int,
                      "external_image": url or null,
                      "image": url or null,
                      "form_factor": int, # id of form factor
                      "socket": int, # id of socket
                      "ram_type": int, # id of RAM type
                      "chipset": int, # id of chipset
                      "producer": int # id of producer
                    },
                "cpu": {
                    "id": int,
                    "created_at": string,
                    "updated_at": string,
                    "status": bool,
                    "name": string,
                    "price": string,
                    "base_clock": float,
                    "turbo_clock": float,
                    "cores": int,
                    "threads": int,
                    "tdp": int,
                    "integrated_graphics": string or null,
                    "external_image": url or null,
                    "image": url or null,
                    "socket": int, # id od socket
                    "producer": int # id of producer
                },
                "ram": {
                    "id": int,
                    "created_at": string,
                    "updated_at": string,
                    "status": bool,
                    "name": string,
                    "size": int,
                    "price": string,
                    "clock": int,
                    "sticks": int,
                    "timings": string,
                    "external_image": url or null,
                    "image": url or null,
                    "type": int, # id of RAM type
                    "producer": int # id of producer
                },
                "gpu": {
                    "id": int,
                    "created_at": string,
                    "updated_at": string,
                    "status": bool,
                    "name": string,
                    "pci_e": int,
                    "vram": int,
                    "cores": int,
                    "price": string,
                    "length": float,
                    "slots": float,
                    "connectors_8pin": int,
                    "connectors_6pin": int,
                    "hdmi": int,
                    "display_port": int,
                    "dvi": int,
                    "vga": int,
                    "boost_clock": int,
                    "memory_clock": int,
                    "tdp": int,
                    "external_image": url or null,
                    "image": url or null,
                    "series": int, # id of series
                    "producer": int, # id of producer
                    "sync": int # id of sync
                },
                "case": {
                    "id": int,
                    "created_at": string,
                    "updated_at": string,
                    "status": bool,
                    "name": string,
                    "price": string,
                    "external_image": url or null,
                    "image": url or null,
                    "type": int # id of type,
                    "color": int, # id of color
                    "side_panel": int, # id of side panel
                    "style": int # id of style
                },
                "internal_drive": {
                    "id": int,
                    "created_at": string,
                    "updated_at": string,
                    "status": bool,
                    "name": string,
                    "price": string,
                    "capacity": int,
                    "price_per_gb": string,
                    "cache": int,
                    "form_factor": string,
                    "interface": string,
                    "external_image": url or null,
                    "image": url or null,
                    "drive_type": int # id of drive type
                },
                "power_supply": {
                    "id": int,
                    "created_at": string,
                    "updated_at": string,
                    "status": bool,
                    "name": string,
                    "price": string,
                    "wattage": int,
                    "external_image": url or null,
                    "image": url or null,
                    "type": int, # id of type
                    "efficiency": int # id of efficiency
                }
            },
          ]
        }
     }

<p align="right">(<a href="#readme-top">back to top</a>)</p>

2. Pick Laptop
   * POST method
   * path
     ```sh
     pick-laptop/
     ```
   * Body
     ```sh
     {
       "field_id": int,
       "budget": num,
     }
     ```
   * Response
     ```sh
     {
      "num_of_laptops": int,
      "laptops": [
          {
             "perc": num,
             "price": num,
             "laptop": {
                  "id": id,
                  "created_at": string,
                  "updated_at": string,
                  "status": bool,
                  "name": string,
                  "screen_size": float,
                  "cpu_type": string,
                  "memory": int,
                  "storage": string,
                  "gpu": string,
                  "vram": int,
                  "gpu_speed": float,
                  "gpu_cores": int,
                  "resolution": string,
                  "weight": float,
                  "backlit_keyboard": bool,
                  "touchscreen": bool,
                  "cpu_speed": float,
                  "number_of_cores": string,
                  "display_type": string,
                  "graphic_type": string,
                  "operating_system": string,
                  "webcam": bool,
                  "price": string,
                  "external_image": url or null,
                  "image": url or null,
              },
           ]
        }
     }

<p align="right">(<a href="#readme-top">back to top</a>)</p>

3. Pick Mobile
   * POST method
   * path
     ```sh
     pick-mobile/
     ```
   * Body
     ```sh
     {
       "field_id": list of int,
       "budget": num,
     }
     ```
   * Response
     ```sh
     {
      "num_of_mobiles": int,
      "mobiles": [
          {
             "perc": num,
             "price": num,
             "mobile": {
                  "id": id,
                  "created_at": string,
                  "updated_at": string,
                  "status": bool,
                  "name": string,
                  "price": string,
                  "cameras": string,
                  "cpu": string,
                  "core_count": int,
                  "cpu_speed": float,
                  "storage": string,
                  "ram": int,
                  "screen_size": float,
                  "refresh_rate": int,
                  "battery": int,
                  "fast_charging": bool,
                  "main_camera": int,
                  "front_camera": int,
                  "cameras_num": int,
                  "external_image": url or null,
                  "image": url or null,
              },
           ]
        }
     }

<p align="right">(<a href="#readme-top">back to top</a>)</p>
