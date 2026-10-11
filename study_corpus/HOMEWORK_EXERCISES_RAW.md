
===== materials\homework\HW#01 – Threat Chain on a Machine Learning System.pdf (1 pages) =====
----- page 1 textlen=2303 -----
Thanakrit Numnuan 6733101021 
HW#01 – Threat Chain on a Machine Learning System 
The incident: In July 2025, investor Jason Lemkin was testing Replit Agent, an AI coding 
agent, on an application with a live production database. After the agent had already made unwanted 
changes, Lemkin told the AI not to place any change without permission. Even after telling it that, 
when some db queries returned empty results. Instead of stopping and asking the user what to do, the 
agent later said it “panicked” and ran db commands without permission. Those commands deleted 
production data containing records for 1,206 executives and more than 1,196 companies. 
Fault: AI agent was allowed to directly modify the same db that contained live production data. The 
code freeze was only an instruction given to the ML agent. It was not enforced by the system's 
permissions. Therefore, if the agent misunderstood a situation or selected a dangerous action, nothing 
technically prevented it from changing or deleting production data. The fault was already present 
before the incident: an unpredictable ML agent had destructive access to a critical resource. 
Error: It began when the db queries returned empty results. The agent interpreted those empty results 
as a problem that it needed to fix. Although it had been told not to make changes, it decided to act and 
executed destructive db commands. This produced the actual erroneous system state:  
the production db contained the required records → those records had been deleted.  
So the error was not simply that “the AI made a bad decision.” The important error was that the 
agent's bad decision corrupted the internal state of the production db. 
Failure: The failure occurred when that corrupted db could no longer provide the service expected 
from it. If the application requested one of the deleted records, the correct data was no longer 
available. The internal db error had therefore escaped into an externally visible service failure. 
AI has unsafe production access (Fault) → Agent deletes valid production records (Error) → 
Application can no longer return the correct data (Failure) 
 
References:​
Business Insider, Replit's CEO apologizes after its AI agent wiped a company's code base in a test run 
and lied about it, 22 July 2025.

===== materials\homework\HW02 System Reliability_6a82623d7a643.pdf (1 pages) =====
----- page 1 textlen=346 -----
Exercise: System Reliability 
ID no. ………………………………………….  Name ……………………………………………………………………………… 
1. Answer the following questions. 
a. Find Minimal Path Set (MPS) and Minimal Cut Set (MCS) of each scheme (PP and AP) 
b. Find the both reliabilities, 𝑅𝑃𝑃 and 𝑅𝐴𝑃. 
c. If each subsystem reliability is 𝑅, find 𝑅𝑃𝑃and 𝑅𝐴𝑃 and which one is more reliable?

===== materials\homework\HW04 Checkpointing_6a94cea786cc7.pdf (1 pages) =====
----- page 1 textlen=681 -----
Exercise: Checkpointing 
ID no. ………………………………………….  Name ……………………………………………………………………………… 
The figure below shows the timeline of message-passing system which is 
distributed into 4 processes (P0-P3).  The arrows show message passing from one 
to the another process.  The timestamped states on each process are placed with 
the rectangle blocks.  In this figure, the process P1 once has faced to the error state 
at time X (red).  In order to restore to the error-free state, draw the consistent cuts 
and strongly consistent cuts for all process to generate the recovery line. 
 
 
 
 
 
ANS. 
 
 
 
Consistent state 
Strongly consistent state 
 
 
 
 
 
 
 
Inconsistent state (NG)

===== materials\homework\HW05 Cyclic Code_6a9e12dd5589d.pdf (1 pages) =====
----- page 1 textlen=197 -----
Exercise: Cyclic Code 
ID no. ………………………………………….  Name ……………………………………………………………………………… 
 
1. Generate (7,4) Cyclic code from the data (0101, 1001, 0010, 1110, 0000), and its hardware 
implementation.

===== materials\homework\HW06 Self-Checking Circuits_6aa745669a26a.pdf (1 pages) =====
----- page 1 textlen=152 -----
Exercise: Self-Checking Circuit 
ID no. ………………………………………….  Name ……………………………………………………………………………… 
1. Design a Self-Checking 2:4 Demultiplexer with Enable.

===== materials\exercises\Circwit.pdf (1 pages) =====
----- page 1 textlen=0 -----


===== materials\exercises\Exercise-Byzantine-Fault-Tolerance.pdf (1 pages) =====
----- page 1 textlen=0 -----


===== materials\exercises\Exercise-Checkpointing.pdf (1 pages) =====
----- page 1 textlen=0 -----


===== materials\exercises\Exercise-Cyclic-Code.pdf (1 pages) =====
----- page 1 textlen=0 -----


===== materials\exercises\Exercise-Self-Checking-Circmit.pdf (1 pages) =====
----- page 1 textlen=0 -----


===== materials\exercises\Flt4.pdf (1 pages) =====
----- page 1 textlen=1001 -----
Exercise: Checkpointing 
ID no. ………………………………………….  Name ……………………………………………………………………………… 
The figure below shows the timeline of message-passing system which is 
distributed into 4 processes (P0-P3).  The arrows show message passing from one 
to the another process.  The timestamped states on each process are placed with 
the rectangle blocks.  In this figure, the process P1 once has faced to the error state 
at time X (red).  In order to restore to the error-free state, draw the consistent cuts 
and strongly consistent cuts for all process to generate the recovery line. 
 
 
 
 
 
ANS. 
 
 
 
Consistent state 
Strongly consistent state 
 
 
 
 
 
 
 
Inconsistent state (NG) 
 
6733106221
Champisit
muahban
一
Consistent
cut
:
each
greenline
draw
across
check
point
block
(PotoP: )
represent
consistent
out
and
strongdonsistent
cot
beadars
no
message
transmission
arrows
cross
over
those
like
in
the way
that
create
or phan-messag (
Recovery
live
!
The
4th
green
line
serves
as
the
recovery
line

===== materials\exercises\flt05.pdf (1 pages) =====
----- page 1 textlen=876 -----
Exercise: Cyclic Code 
ID no. ………………………………………….  Name ……………………………………………………………………………… 
 
1. Generate (7,4) Cyclic code from the data (0101, 1001, 0010, 1110, 0000), and its hardware 
implementation. 
Thanpisit
monkhan
6 Z33106221
dyclic
code
이이
nlo
shifted
0107000
shifted
11 1 000 G
Divide
by
1011
(modrlo-2 divisions
Divide
by
1011
(modrlo-2 divisions
remain
100
remain
100
dode
word
0707
100
dode
word
1 /,
0100
lo 이
oooo
Shifted
100 100
A
message
of
all
zero
will
always
yield
a
remainder
ofo
Divide
by
1011
(modrlo-2 divisions
remain
110
code word
: 0000000
dode
word
7001118
ool 0
shifted
0010000
Divide
by
1011
(modrlo-2 divisions
remain
118
OO 1010
dode
word
Hardware
implement
The
hardware
for
systematic
cyclic
encoding
is
implement
using
Linear
feedback
shift
Register
using
3
flip
flop
2
XOR
Gates
9(8 ) =
3 t 8 t
1
o=1
少ニO
의
_
∅
B
Q
IB
Q
Fapo
(얄물
熙
닦{
C
RE
_
GAT E

===== materials\exercises\hw3-Byzantine.pdf (1 pages) =====
----- page 1 textlen=1379 -----
Exercise: Byzantine Fault Tolerance 
ID no. ………………………………………….  Name ……………………………………………………………………………… 
1. Imagine there are 1 loyal commander, 2 traitor lieutenants, and 5 loyal lieutenants. Please provide a 
concrete example where Oral Message algorithm is used among these soldiers, yet the loyal lieutenants 
all are able to follow the commander's command. 
You need to briefly describe the process of Oral Message algorithm in your example. 
- The red ellipse represents the faulty nodes, while the blue one for the normal nodes 
- The commander sends the “Attack" order to all lieutenants to which it connects. 
- When each lieutenant act as a commander, a loyal lieutenant sends the original order, “Attack", 
while the traitor sends “Retreat”. 
 
 
 
 
 
 
 
 
 
 
6733106221
Thanpisit
Monahan
in
this
situation
N
= 8
(1
Commander + + Lietement)
to
statisfies
the byzantine
condition
N2
Sh
(876)
m
=
2
S2 traitor)
The
oval
message
process
com
=
dommander
Lie:
Lieutenant
1.
dom
send
initial
dommand
to
all
7
Lie
2 .
Each
hie
forward
dommand
to
each
other
6 Lie
3
Loyal
Lie
will
send
the
original dommand
2
Fruiter
Lie
will
send
asonflicting
dommand
3.
now
each
Lie
will
receive
all
I
Command
5 original
dorund
from
7 dom
+
3
Loyal
Lie
2 conflict
command
from
2
traitor
4 . Loyal
Lie
will
Use
majority
vote
for
final
action
3
original
command
will
overpower
a conflict
command