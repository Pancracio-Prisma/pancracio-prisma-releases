# Panky para tu empresa

<p align="center"><picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/panky-logo-dark.svg">
  <img src="assets/panky-logo-light.svg" alt="Panky" width="260">
</picture></p>

Panky es un asistente que recuerda el trabajo de una organización y ayuda a
encontrar, actualizar y compartir lo que corresponde a cada persona. Puedes
hablar con él desde Codex, Claude Code, Gemini CLI o Antigravity. El historial
de cada aplicación puede ser distinto; el contexto de trabajo publicado y tus
permisos siguen siendo los mismos.

## Qué puede hacer

- Encontrar información de tu equipo y citar de dónde salió.
- Guardar avances que conviene recordar y comprobar que quedaron disponibles.
- Ayudarte con documentos, recursos y herramientas que tu empresa conectó.
- Guiar altas, cambios de puesto, permisos y bajas cuando tu cuenta tiene
  autorización para ello.
- Mantener aparte tus notas personales. Cambiar de interfaz de IA no abre el
  contexto de otra persona.

Panky no adivina permisos por tu cargo ni porque hayas recibido un enlace. Tu
empresa define quién puede leer o modificar cada contexto y recurso. Panky
comprueba tu cuenta de trabajo y la política vigente antes de mostrar o hacer
algo. Las acciones de administración disponibles dependen de tu Seat activo;
si una acción no está permitida, no aparece como opción para ti.

## Cómo funciona la seguridad

El **Core** de la empresa registra su estructura, los puestos y las reglas.
El **Prisma Gateway** comprueba tu inicio de sesión con Google, consulta esas
reglas y conecta las herramientas aprobadas, como Google Workspace. Antes de
cada acción vuelve a verificar tu acceso. GitHub transporta los archivos de
contexto entre instalaciones, pero una llave de GitHub no sustituye tus
permisos en Panky. Los cambios importantes dejan un recibo y se publican en
una versión revisada del Core.

Durante una prueba de concepto, la empresa puede usar una cuenta GitHub de
transporte compartida; cada computadora recibe su propia llave. Tu cuenta
Google de trabajo sigue identificándote y limitando lo que Panky te muestra.
Quien tenga una de esas llaves puede acceder directamente por Git a los
repositorios concedidos a la cuenta compartida. La empresa debe tratarla como
una credencial de prueba y retirarla al pasar a cuentas individuales.

## Cómo empezar

El administrador prepara la empresa una vez y te entrega un ZIP firmado.
Extrae el ZIP y abre esa carpeta en tu agente de IA preferido. El agente
comprueba el paquete, instala la versión firmada disponible y te guía por el
inicio de sesión con Google. No compartas contraseñas ni códigos en el chat.

- [Instalación para cada persona](docs/END_USER_INSTALL.md)
- [Instalación técnica de la empresa](docs/TECH_INSTALL.md)

Necesitas Visual Studio Code, la interfaz de IA que prefieras y un plan que
permita usar ese agente. Para el uso cotidiano, considera un plan de pago de
entrada cercano a USD 20 al mes; los precios y límites dependen del proveedor.

## Las altas que puedes pedirle

La preparación técnica ocurre una vez por empresa. Después, cada persona
instala su copia y Panky la ayuda a conocer su puesto. Las demás altas se
piden cuando la empresa necesita incorporar o cambiar algo. Panky hará las
preguntas que falten y mostrará el resultado antes de aplicar cambios que
afecten a otras personas.

| Alta o cambio | Mensaje de ejemplo |
| --- | --- |
| Preparar la empresa | “Instala Panky Prisma para esta empresa siguiendo la guía técnica y ayúdame a definir su estructura y accesos.” |
| Instalar para una persona | “Instala Panky Prisma con el ZIP de esta carpeta, verifica el paquete y acompáñame hasta que quede listo.” |
| Conocer el trabajo de una persona | “Soy Andrea, acabo de entrar a FP&A. Ayúdame a entender mi puesto, mi equipo y los asuntos en curso.” |
| Departamento | “Crea el departamento de Finanzas bajo Dirección y prepara su contexto.” |
| Puesto y persona | “Da de alta a Andrea en FP&A con su correo corporativo y revisa qué acceso necesita.” |
| Herramienta | “Conecta nuestro servicio de facturación y dime qué autorización necesita.” |
| Recurso | “Conecta la carpeta de presupuestos al equipo de Finanzas.” |
| Compartir acceso | “Quiero que este puesto pueda leer el tablero de gastos.” |
| Espacio restringido | “Crea un espacio para el cierre mensual y muéstrame quién podría verlo.” |
| Cambio de puesto | “Andrea pasa a Operaciones el próximo mes; revisemos qué cambia.” |
| Baja | “Da de baja a esta persona y comprueba que perdió el acceso.” |

También se pueden configurar roles, herramientas, excepciones y transferir la
responsabilidad de Founder. Esas acciones requieren la autoridad
correspondiente; Panky solo ofrece las que tu cuenta puede solicitar. La
desinstalación local de Panky es distinta de dar de baja a una persona en la
empresa.

## Novedades

- **0.2.8:** la empresa puede cambiar el nombre visible de Panky mediante una
  configuración firmada. También puede recuperarse una actualización con un
  kit nuevo cuando una versión instalada aún no conoce ese flujo.
- **0.2.7:** mejora la búsqueda de hechos relacionados entre fuentes que la
  persona ya puede leer, conservando la referencia a cada fuente.
- **0.2.6:** presenta respuestas con bloques enriquecidos de forma coherente
  entre las interfaces de IA compatibles.
- **0.2.5:** equilibra la recuperación de contexto y mejora la corrección de
  hechos publicados.

Las versiones firmadas para macOS y Windows aparecen en la sección
[Releases](https://github.com/Pancracio-Prisma/pancracio-prisma-releases/releases).
Un ZIP preparado para una empresa no debe instalarse en otra.
