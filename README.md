# tuGerente_test
Interview Test de tuGerente hecho con Django y Djangorestframework.

Para correr este test seguir estos pasos:
- Migrar los modelos a la base de datos con python manage.py migrate (la BD es sqlite)
- Correr el servidor virtual con python manage.py runserver
# Endpoints 
Todos los endpoints mencionados son con el método POST.
- /clients
- /rooms
- /reserves

# Workflow
1. Crear cuartos para alojamiento con el endpoint '/rooms', seleccionando un estilo de cuarto entre las opciones ['SINGLE', 'TWIN', 'DOUBLE', 'DELUXE'].
2. Registrar un cliente con su nombre, apellido y numero de identificación en el endpoint '/clients'.
  Parametros:
    - first_name
    - last_ name
    - dni
3. Reservar un cuarto del hotel en el endpoint '/reserves' mediante los siguientes parametros:
  - client = ID del cliente registrado
  - room = ID del cuarto registrado
  - end_date = Fecha final de la estadía en formato mm / dd / yyyy 
  - state = Estado de la reservación, opciones ['PAID', 'PENDING', 'ELIMINATED']
  - paid_amount = Monto pagado de la reservación, formato decimal.
  - pay_method = Método de pago para la reservación, opciones ['CASH', 'CREDIT', 'DEBIT', 'CHECK', 'TRANSFER']
