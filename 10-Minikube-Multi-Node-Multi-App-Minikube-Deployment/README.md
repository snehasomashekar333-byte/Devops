# Exercise 10: Multi-Node Kubernetes Cluster
## Objective
Deploy a Product Catalog and Shopping Cart application on a multi-node Minikube cluster using Kubernetes Deployments and Services.
## Technologies Used
- Docker
- Minikube
- Kubernetes
- Python and Flask
- PowerShell
## Applications
### 1. Product Catalog
- Application file: `product_catalog.py`
- Dockerfile: `Dockerfile.product`
- Endpoint: `GET /products`
- Returns a list of products, including Laptop, Phone, and Headphones.
### 2. Shopping Cart
- Application file: `shopping_cart.py`
- Dockerfile: `Dockerfile.shopping`
- Endpoints: `GET /cart` and `POST /cart`
- Supports viewing the cart and adding items.
## Kubernetes Configuration
- `product_catalog_deployment.yaml`: Configures 2 Product Catalog replicas.
- `shopping_cart_deployment.yaml`: Configures 3 Shopping Cart replicas.
- `product_catalog_service.yaml`: Defines the Product Catalog Service.
- `shopping_cart_service.yaml`: Defines the Shopping Cart Service.
Pod anti-affinity rules are configured to require replicas of each application to run on different nodes.
## Docker Images
- `product-catalog:latest`
- `shopping-cart:latest`
## Project Structure
- `Dockerfile.product`
- `Dockerfile.shopping`
- `product_catalog.py`
- `shopping_cart.py`
- `product_catalog_deployment.yaml`
- `product_catalog_service.yaml`
- `shopping_cart_deployment.yaml`
- `shopping_cart_service.yaml`
- `screenshots/`: Exercise screenshots.
## Deployment Workflow
1. Start Docker Desktop and Minikube.
2. Configure a multi-node Minikube cluster.
3. Build the Docker images.
4. Apply the Kubernetes Deployments and Services.
5. Verify pod placement, application endpoints, and service availability.
## Verification Status
The original exercise documentation reports that all three nodes became Ready, all five application pods ran successfully, both Services were created, and both applications were tested.
The deployment has not yet been independently reverified in the current environment.
## Screenshots
See the `screenshots` folder for the available exercise screenshots.
