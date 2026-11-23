# Instala Panky Prisma en tu computadora

Esta guía es para cada persona de la empresa. La empresa ya preparó Panky.
El agente que elijas (Codex, Claude Code, Gemini CLI o Antigravity) te ayudará
a instalar tu copia y comprobar que quedó lista.

## Antes de empezar

Instala **Visual Studio Code** y la interfaz del agente de IA que prefieras:
Codex, Claude Code, Gemini CLI o Antigravity. Inicia sesión en ese proveedor y
comprueba que tu plan permite usarlo en VS Code. Para el uso cotidiano, prevé
un plan de pago de entrada cercano a USD 20 al mes; el precio y los límites
dependen del proveedor. También necesitarás la cuenta Google de trabajo que
tu empresa dio de alta en Panky.

## Lo que necesitas recibir

El administrador te entregará **un ZIP de instalación** para tu empresa y tu
sistema (`macos` o `windows`). Su nombre empieza con `Pancracio-Prisma-`.
Al extraerlo encontrarás un aviso de verificación cuyo nombre termina en
`-verification.md`. El agente comprobará las firmas; tú no necesitas
interpretar sus números.

Esto funciona tanto en POC como en modo definitivo. Si falta el aviso dentro
de la carpeta extraída, pídelo al administrador. Recibe el ZIP de la persona que
administra Panky en tu empresa.

## Cómo empezar

Descarga el ZIP y extráelo en tu computadora. Abre **la carpeta extraída**
`Pancracio-Prisma-<empresa>-<macos|windows>-v<versión>` como carpeta de trabajo
en el agente que elijas. No abras una carpeta de otro Panky que ya uses.
Comparte con el agente la carpeta extraída; encontrará ahí el aviso de
verificación.

Dile al agente:

> Instala Panky Prisma en esta computadora siguiendo las instrucciones de
> esta carpeta. Comprueba el aviso de verificación que acompaña al kit,
> guíame hasta que quede listo y conserva cualquier otro Pancracio que ya
> tenga.

Este mensaje sirve para cualquier empresa: la carpeta contiene su
configuración firmada. El agente lee `AGENT_END_USER_INSTALL.md` dentro de ella,
comprueba el paquete y busca la versión firmada más reciente **antes de la
primera instalación**. El número en el nombre del ZIP indica la versión con
que se preparó el kit; no limita la versión que quedará instalada. Si no se
puede comprobar el canal o la firma, el agente se detiene y te explica el motivo.
No tienes que ejecutar comandos ni proporcionar identificadores de la empresa.

## Lo que te pedirá la instalación

El agente te guiará para iniciar sesión con **tu cuenta Google de trabajo**. Si
Google muestra una pantalla de permisos, revisarás y aprobarás allí el acceso
que Panky solicita para trabajar con Google Workspace, como Drive, Docs o
Sheets. Panky actúa con tu cuenta dentro de lo que Google te permite y de los
permisos que tu empresa haya configurado. Esta aprobación no le da acceso a
otras cuentas tuyas. Escribe contraseñas y códigos solo en la página de
Google; nunca los pegues en el chat.

Si tu empresa está en **modo POC**, no necesitas cuenta GitHub, una sesión
abierta en GitHub ni una llave SSH preparada en tu computadora. El kit ya
indica la cuenta de transporte de la empresa. Durante la instalación, el agente
crea una llave distinta para esta computadora, el Gateway la registra y
comprueba que la instalación trae los repositorios autorizados para tu
cuenta de trabajo. No te pedirá esa llave ni un token en el chat. Si la
comprobación falla, no declarará la instalación lista.

Fuera del POC, el agente te guiará para conectar tu cuenta GitHub individual y
verificará sus accesos antes de traer información de la empresa.

## Al terminar

Panky traerá el contexto de trabajo que te corresponde. Tu espacio personal
quedará separado. Durante el POC permanecerá en esta computadora; cuando la
empresa pase a modo definitivo podrás elegir una copia privada.

El agente te dirá cuándo la instalación esté **lista** y Panky te hará unas pocas
preguntas para empezar a trabajar contigo. Si falta el aviso, la autorización
de Google o algún acceso, el agente te dirá exactamente qué necesita del
administrador y no dará por terminado el proceso.

Al quedar lista, el agente abre una ventana nueva de VS Code en la **carpeta de
trabajo instalada**, abre el chat del proveedor que elegiste y envía un primer
«Hola, Panky» (o el nombre que configuró tu empresa). Comprueba que Panky
responde con tu identidad y tus permisos. No tienes que buscar la carpeta ni
escribir ese saludo. Si el chat pide iniciar sesión, confiar en la carpeta o
aprobar una herramienta, completa ese paso en la interfaz y el agente continúa.
Si no puede verificar la respuesta, mantiene el primer chat pendiente y te
explica qué bloqueó el traspaso.

Para tus chats siguientes, abre esa misma carpeta con el agente que prefieras.
En Windows para Headquarters suele estar en
`C:\Users\<tu usuario>\Pancracio Prisma\instances\headquarters\workspace`.
La carpeta extraída del ZIP sirve para instalar, no para el uso diario. Si el
alta queda pendiente, continúa el chat de instalación desde el estado guardado
hasta que el agente confirme que está lista; no reinstales para retomar.

Al abrir por primera vez esa carpeta en Claude Code, Gemini CLI o Antigravity, la aplicación
puede pedirte confiar en la carpeta o permitir las herramientas de Panky.
Comprueba que muestra la ruta de esta instancia; el agente debe usar tu
identidad de Google y las mismas reglas de acceso, aunque cambies de chat.
El historial de mensajes de una aplicación no se copia a las otras.

## Si quieres desinstalar esta copia

Dile al agente: «Desinstala Panky Prisma de esta computadora». El agente te mostrará
la empresa y la instancia exactas y te pedirá confirmar esa instancia. Luego
detendrá su sincronización, revocará su llave de GitHub y sus credenciales de
transporte, y borrará solo sus carpetas locales. Esto incluye el contexto
personal que estuviera guardado únicamente en esa copia; pide conservar una
copia antes de confirmar si la necesitas. Si una revocación falla, el agente dejará
la instalación recuperable para reintentar y no dirá que se desinstaló.

Desinstalar tu computadora **no** da de baja tu cuenta de Panky en la empresa,
ni cambia tus Seats o permisos. Esa baja se solicita por separado a la empresa.

Para futuras actualizaciones, basta decir: **«Panky, actualízate»**.

Si la empresa termina el POC, Panky te avisará cuando llegue el cambio desde
Core. Te mostrará la cuenta GitHub asignada y te preguntará qué perfil de
Chrome la tiene abierta. El agente preparará la conexión, la llave y los accesos;
GitHub puede pedirte aprobar una invitación. No tendrás que reinstalar Panky
ni escribir comandos o compartir claves en el chat.
