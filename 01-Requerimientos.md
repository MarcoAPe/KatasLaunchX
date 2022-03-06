# 1. Descripción general del requerimento

|           **Proyecto**          | Aplicación capaz de automatizar el proceso de recepción de casos de demanda y simplificar la comunicación entre el solicitante y asesor legal. |
|:-------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------------:|
|            **Nombre**           |                                                                    Abogabot                                                                    |
|      **Fecha de solicitud**     |                                                                   20/02/2022                                                                   |
|   **Responsable de solicitud**  |                                                                Rodrigo Martínez                                                                |
| **Dependencia del solicitante** |                                                               Innovaccion Virtual                                                              |
|    **Responsable funcional**    |                                                                   Marco Pérez                                                                  |
# 2. Formalización
|                                                                                                                                                                                                                                                                                                                                                                                                                                       **DESCRIPCIÓN DE LA SOLICITUD**                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|                                                                                                                                                                                                                                                                                                                                                                                                                                           **Solcitante: Rodrigo Martínez**                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Es un despacho de abogados que quiere automatizar las demandas de sus clientes, esto lo harán a través de una página web, llenando un formulario. Al momento de llenar el formulario se manda al proceso de pago para finalizar la transacción. Para dar seguimiento a su demanda, el cliente crea una cuenta en la plataforma y verá el seguimiento de cada una de las actualizaciones del proceso legal. El administrador del sitio recibe la notificación de una nueva demanda y con los datos llenados del formulario se crea automáticamente el documento legal en formato word para empezar el proceso. El administrador recibe el pago y debe de ser capaz de verlo en un dashboard para ver la cantidad de ingresos recibidos. El administrador actualiza el proceso de la demanda y agrega comentarios en cada paso del proceso. La página debe ser responsive para poder verla desde el celular. |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             **Líder funcional: Marco Pérez**                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Se requiere crear una aplicación capaz de automatizar la solicitud, proceso y recepción de una demanda desde la emisión y pago de los servicios por parte del solicitante, hasta la recepción por parte del asesor legal que prestará sus servicios, todo esto en formato word. La aplicación debe notificar al solicitante cada vez que haya una modificación en el proceso legal, en donde podrá conocer detalles adicionales proporcionados por el asesor, acerca de cada paso. Debe ser accesible especialmente desde dispositivos móviles y ser fácil de manipular.                                                                                                                                                                                                                                                                     

##### Firmas de conformidad

|           ____________________________________          |        ___________________________________        |
|:-------------------------------------------------------:|:-------------------------------------------------:|
| Rodrigo Martínez\| Innovaccion Virtual | Marco Pérez\| Departamento de TI |
# 3. Análisis de requisitos y requerimentos
Nuestro despacho de abogados constituido por:
- **Parte administrativa.**
    - Atención al cliente.
    - Contabilidad.
    - Marketing.
    - Recursos humanos.
- **Parte técnica.**
    - Servicios.
        - Personas físicas y morales.
            - Asesoría puntual.
            - Seguimiento de caso.
        - Agencia de auditoría.
    - Manejo de la información.
    - Tipo de abogacía requerida.*

###### *Penal, civil, comercial, laboral, tributaria, constitucional, administrativa, etc.

Trabaja actualmente de la siguiente forma en lo que solicitar un servicio refiere:
![1stOrganization](/images/uno.jpg)

Abogabot estaría soportado de la mayoría de las áreas en algún aspecto por lo que su adición reorganizaría el proceso (áreas involucradas directamente):

- En un <span style="color:green">primer paso</span> Abogabot filtra las necesidades del cliente para analizarse y decidirse los servicios requeridos.
- En un <span style="color:orange">segundo paso</span> se costean los requerimentos del caso y se realiza el cobro.
- En un <span style="color:purple">último paso</span> paso toda la información es proporcionada al asesor legal y lo comunica directamente con el solicitante.

En conjunto se logra involucrar más a todas las áreas en el proceso sin llegar a sobrecargarlas, agilizando el contacto con el cliente y simplificando la identificación de fallos.