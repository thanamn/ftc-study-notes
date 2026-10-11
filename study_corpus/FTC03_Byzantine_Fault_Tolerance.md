# FTC03_Byzantine_Fault_Tolerance

> Source: `2110473_2026S1_FTC03_Byzantine_Fault_Tolerance-9294-17875577778080.pdf` — 36 slides. `visual: true` slides have a rendered image in `images/`.

## Slide 1: Home Exercise: Reliability  *(visual)*
R1 R2 B2 R3 R4 Sys Probability
 PP scheme 1 1 1 1 1 1

 1 1 1 1 0 1
 R1R2
 - - - - - -

 1 1 0 0 0 1

 1 0 1 1 1 1 R1R2'B2R3R4

 1 0 1 1 0 0 0

 1 0 1 0 1 1 R1R2'B2R3'R4
 Bridge 1 0 1 0 0 0 0
R1 R2 - - - - - -

 0 0 0 0 0 0 0

 R1 = (1-(1-RA)2) Rbridge = R1R2 + R1R2'B2R4 +
 R2 = RBRC R1'R2B2R3 + R1'R2B2'R3R4 +R3 R4
 R3 = RARB R1'R2'R3R4
 R4 = (1-(1-RC)2) 1
![FTC03_Byzantine_Fault_Tolerance slide 1](images/FTC03_Byzantine_Fault_Tolerance_s001.png)

## Slide 2: Byzantine Fault Tolerance
(Fault Tolerance in Distributed Systems)

 2110473 Fault Tolerant Computing

 Several sources

## Slide 3: Contents
• Process Groups
• Fault Tolerance in Process Groups
• Byzantine Generals Problem
• Oral Message Algorithm
• Blockchain
• Reliable Client-Server Communication

## Slide 4: Process Groups  *(visual)*
➢All members of a group receive a message sent to the group
 ➢If one process fails, others can take over
 ➢Can be dynamic; processes can have multiple memberships

(a) Communication in a flat group: No Single Point-of-Failure, Complicated Decision Making
(b) Communication in a hierarchical group: Single Point-of-Failure, Quick Decision Making
![FTC03_Byzantine_Fault_Tolerance slide 4](images/FTC03_Byzantine_Fault_Tolerance_s004.png)

## Slide 5: Process Group Architecture  *(visual)*
Central Authority Consensus Protocol
 (Agreement)
![FTC03_Byzantine_Fault_Tolerance slide 5](images/FTC03_Byzantine_Fault_Tolerance_s005.png)

## Slide 6: Centralized & Distributed Ledger  *(visual)*
6
![FTC03_Byzantine_Fault_Tolerance slide 6](images/FTC03_Byzantine_Fault_Tolerance_s006.png)

## Slide 7: Process Group Resilience
❑Organize several identical processes into a group
❑When a message is send to a group, all members of the
 group receives it
❑If one process in a group fails (no matter what reason),
 hopefully some other process can take over for it
❑The purpose of introducing groups is to allow processes
 to deal with collections of processes as a single
 abstraction.
❑Important design issue is how to reach agreement within
 a process group when one or more of its members cannot
 be trusted to give correct answers.

## Slide 8: Fault Tolerance in Process Groups
❑A system is k fault tolerant if it can survive faults in k components and
 still meet its specification
❑If failures are safe (silent), then k+1 processes are sufficient to get k
 fault tolerance
❑In case of arbitrary failures, 2k+1 processes are required (since k failing
 processes can all generate the same result by chance)
 ❑This assumes that each process reaches its decision independently
 ❑What if processes gang up to produce wrong results? General
 problem is having a process group reach an agreement
 ❑In this case you need 2k+1 correctly functioning processes, for a
 total of 3k+1 processes
❑In both cases we assume that communication failures do not occur

## Slide 9: Byzantine Generals Problem  *(visual)*
9
![FTC03_Byzantine_Fault_Tolerance slide 9](images/FTC03_Byzantine_Fault_Tolerance_s009.png)

## Slide 10: Agreement: Byzantine Generals Problem (1)  *(visual)*
How does a process group deal with a faulty member?

❑The "Byzantine Generals Problem" for 3 loyal generals and 1 traitor.
a) The generals announce their troop strengths to the other members of the group by
 sending a message.
b) The vectors that each general assembles based on (a), each general knows their own
 strength. They then send their vectors to all the other generals.
c) The vectors that each general receives in step 3. It is clear to all that General 3 is the
 traitor. In each 'column', the majority value is assumed to be correct.
![FTC03_Byzantine_Fault_Tolerance slide 10](images/FTC03_Byzantine_Fault_Tolerance_s010.png)

## Slide 11: Agreement: Byzantine Generals Problem (2)  *(visual)*
Warning: the algorithm does not always work! ⇒Two-Army Problem

• The same algorithm as in previous slide, except now with 2 loyal generals
 and 1 traitor. Note: It is no longer possible to determine the majority value
 in each column, and the algorithm has failed to produce agreement.
• It has been shown that for the algorithm to work properly, more than two-
 thirds of the processes have to be working correctly. That is: if there are M
 faulty processes, we need 2M + 1 functioning processes to reach agreement.
![FTC03_Byzantine_Fault_Tolerance slide 11](images/FTC03_Byzantine_Fault_Tolerance_s011.png)

## Slide 12: Oral Messages
Byzantine Agreement (n nodes, m faults)
 - can be reached using Oral Messages,
 if n >= 3m+1

Assumptions:
• Every message is delivered correctly
• Receiver knows who sent message
• Absence of message can be detected

## Slide 13: Oral Message Algorithm
OM(0)
1. Commander sends his value to every lieutenant
2. Each lieutenant uses the received value or "retreat" if no
 value received

OM(m)
1. Commander sends his value to every lieutenant
2. Everyone runs OM(m-1) and acts as the commander to
 send the value received in step 1 to all the other lieutenant
3. Each lieutenant uses the majority value out of the values
 received
 Recursive Algorithm
 (No solution with fewer than 3m+1 generals can cope with m traitors)

## Slide 14: Example: Bad Lieutenant  *(visual)*
Scenario: m=1, n=4, traitors=L3
![FTC03_Byzantine_Fault_Tolerance slide 14](images/FTC03_Byzantine_Fault_Tolerance_s014.png)

## Slide 15: Example: Bad Commander  *(visual)*
Scenario: m=1, n=4, traitors=C
![FTC03_Byzantine_Fault_Tolerance slide 15](images/FTC03_Byzantine_Fault_Tolerance_s015.png)

## Slide 16: Bigger BFT (Bad Lieutenants )  *(visual)*
Scenario: m=2, n=7, traitors=L5,L6

Decision??

 https://github.com/AnantJoshiCZ/Byzantine
 https://github.com/AnantJoshiCZ/Byzantine
![FTC03_Byzantine_Fault_Tolerance slide 16](images/FTC03_Byzantine_Fault_Tolerance_s016.png)

## Slide 17: Bigger BFT (Bad Commander+ )  *(visual)*
17
![FTC03_Byzantine_Fault_Tolerance slide 17](images/FTC03_Byzantine_Fault_Tolerance_s017.png)

## Slide 18: Decision with Bad Commander+  *(visual)*
18
![FTC03_Byzantine_Fault_Tolerance slide 18](images/FTC03_Byzantine_Fault_Tolerance_s018.png)

## Slide 19: Next Step of Algorithm  *(visual)*
19
![FTC03_Byzantine_Fault_Tolerance slide 19](images/FTC03_Byzantine_Fault_Tolerance_s019.png)

## Slide 20: Check Yourself  *(visual)*
Imagine there are 1 loyal commander, 1 traitor lieutenant, and 4 loyal
lieutenants. Please provide a concrete example where Oral Message
algorithm is used among these soldiers, yet the loyal lieutenants all are
able to follow the commander's command.
 You need to briefly describe the process of Oral Message algorithm in
your example.

 A A LIEUTENANT COMMANDER LIEUTENANT

 A A A

 LIEUTENANT LIEUTENANT LIEUTENANT

 - The red ellipse represents the faulty nodes, while the blue one for the normal nodes
 - The commander sends the "Attack" order to all lieutenants to which it connects.
 - When each lieutenant act as a commander, a loyal lieutenant sends the original order, "Attack",
 while the traitor sends "Retreat". 20
![FTC03_Byzantine_Fault_Tolerance slide 20](images/FTC03_Byzantine_Fault_Tolerance_s020.png)

## Slide 21: Check Yourself - Solution (1/3)  *(visual)*
A A LIEUTENANT COMMANDER LIEUTENANT

 A A A

 LIEUTENANT LIEUTENANT LIEUTENANT

 A AOM(1) L C L
 A A A
 L L L
![FTC03_Byzantine_Fault_Tolerance slide 21](images/FTC03_Byzantine_Fault_Tolerance_s021.png)

## Slide 22: Check Yourself - Solution (2/3)  *(visual)*
A AOM(1) L C L L5
 A A A
 L L L

OM(0)

 R AC L L L L L A A
R R R A
 A A A
 L L L C L A L L C L

 A L L L C A A A

 L A L A C L A L A L
![FTC03_Byzantine_Fault_Tolerance slide 22](images/FTC03_Byzantine_Fault_Tolerance_s022.png)

## Slide 23: Check Yourself - Solution (3/3)  *(visual)*
Lieute Value Frm Frm Frm Frm Frm Majority
 nant frm C L1 L2 L3 L4 L5 Vote
 L1 A - A A A R A
 L2 A A - A A R A
 L3 A A A - A R A
 L4 A A A A - R A
 L5 x x x x x - x
![FTC03_Byzantine_Fault_Tolerance slide 23](images/FTC03_Byzantine_Fault_Tolerance_s023.png)

## Slide 24: Number of Messages
Number of Messages
 = (n-1)*(n-2)*…*(n-m-1)
 = O(nm)

 Exponential in number of Traitors!!

• Practical Byzantine Fault Tolerance
• Signed Message Solution

## Slide 25: Practical BFT  *(visual)*
- Client waits for m+1 replies from different replicas with
 same answer
- If primary is faulty, select new primary
- Many optimizations to reduce overhead
![FTC03_Byzantine_Fault_Tolerance slide 25](images/FTC03_Byzantine_Fault_Tolerance_s025.png)

## Slide 26: Blockchain
• A solution to the Byzantine Fault Tolerance
 - For any m, Algorithm OM(m) reaches consensus if
 there are more than 3m generals and at
 most m traitors.
• Remove the middleman while providing a trusted
 exchange
• Power of Blockchain
 - Decentralized, self-governing network (no middleman)
 - Trusted network despite a lack of central governance
• Proof of Work/ Proof of Stake Algorithm

## Slide 27: Proof of Work in Bitcoin  *(visual)*
27
![FTC03_Byzantine_Fault_Tolerance slide 27](images/FTC03_Byzantine_Fault_Tolerance_s027.png)

## Slide 28: BlockChain: Proof of Work  *(visual)*
28
![FTC03_Byzantine_Fault_Tolerance slide 28](images/FTC03_Byzantine_Fault_Tolerance_s028.png)

## Slide 29: BlockChain: Proof of Work  *(visual)*
29
![FTC03_Byzantine_Fault_Tolerance slide 29](images/FTC03_Byzantine_Fault_Tolerance_s029.png)

## Slide 30: Reliable Client-Server Communication
❑Fault Tolerance in DS considers Communication Failures
 o masking crash and omission failures
❑Reliable Point-to-Point (P2P) communication is established
by a reliable transport protocol, such as TCP
 o P2P TCP masks omission failures by guarding against lost messages
 using ACKs and retransmissions
 o But perform poorly when a crash occurs
❑In client/server model, In the case of process failure the
following situations need to be dealt with:
 ➢Client unable to locate server
 ➢Client request to server is lost
 ➢Server crash after receiving client request
 ➢Server reply to client is lost
 ➢Client crash after sending server request

## Slide 31: Lost Request Messages when Server Crashes  *(visual)*
A server in client-server communication
a) Normal case
b) Crash after execution
c) Crash before execution
![FTC03_Byzantine_Fault_Tolerance slide 31](images/FTC03_Byzantine_Fault_Tolerance_s031.png)

## Slide 32: Solutions to Handle Server Failures (1)
➢Client unable to locate server, e.g. server down, or
server has changed
Solution:
 - Use an exception handler - but this is not always
possible in the programming language used

➢Client request to server is lost
Solution:
 - Use a timeout to await server reply, then re-send - but
be careful about idempotent operations (no side effects
when re-send)
 - If multiple requests appear to get lost assume 'cannot
locate server' error

## Slide 33: Solutions to Handle Server Failures (2)
➢Server crash after receiving client request
 Problem may be not being able to tell if request was carried out (e.g.
client requests print page, server may stop before or after printing,
before acknowledgement)
Solutions:
 - rebuild server and retry client request (assuming 'at least once'
semantics for request)
 - give up and report request failure (assuming 'at most once'
semantics), what is usually required is exactly once semantics, but this
difficult to guarantee

➢Server reply to client is lost

 Client can simply set timer and if no reply in time assume server
down, request lost or server crashed during processing request.

## Slide 34: Solutions to Handle Client Failures
➢Client crash after sending server request : Server unable to reply to
client (orphan request)

Options and Issues:
 - Extermination: client makes a log of each RPC, and kills orphan after
reboot. Expensive.
 - Reincarnation. Time divided into epochs (large intervals). When
client restarts it broadcasts to all, and starts a new time epoch. Servers
dealing with client requests from a previous epoch can be terminated.
Also unreachable servers (e.g. in different network areas) may later reply,
but will refer to obsolete epoch numbers.
 - Gentle reincarnation, as above but an attempt is made to contact the
client owner (e.g. who may be logged out) to take action
Expiration, server times out if client cannot be reached to return reply

## Slide 35: Reliable Communication Systems
Examine Assumptions:

➢Synchronous Communication
➢Absence of message can be detected
➢Every message that is sent is delivered correctly
➢Receiver of a message knows who sent it
➢A loyal general's signature cannot be forged, and any
 alteration of the contents of his signed message can be
 detected
➢Anyone can verify the authenticity of a general's signature

## Slide 36: HW03: BFT  *(visual)*
Imagine there are 1 loyal commander, 2 traitor lieutenants, and 5
loyal lieutenants. Please provide a concrete example where Oral
Message algorithm is used among these soldiers, yet the loyal
lieutenants all are able to follow the commander's command.
 You need to briefly describe the process of Oral Message algorithm in
your example.

 A A LIEUTENANT COMMANDER LIEUTENANT
 A A
 LIEUTENANT A A A LIEUTENANT

 LIEUTENANT LIEUTENANT LIEUTENANT

 - The red ellipse represents the faulty nodes, while the blue one for the normal nodes
 - The commander sends the "Attack" order to all lieutenants to which it connects.
 - When each lieutenant act as a commander, a loyal lieutenant sends the original order, "Attack",
 while the traitor sends "Retreat". 36
![FTC03_Byzantine_Fault_Tolerance slide 36](images/FTC03_Byzantine_Fault_Tolerance_s036.png)
