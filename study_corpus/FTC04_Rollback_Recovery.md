# FTC04_Rollback_Recovery

> Source: `2110473_2026S1_FTC04_Rollback_Recovery-9294-17881367582371.pdf` — 51 slides. `visual: true` slides have a rendered image in `images/`.

## Slide 1: Home Exercise: BFT (1/2)  *(visual)*
OM(2): Commander sends A (Attack) to all 7 lieutenants (incl. traitors)

 A A TRAITOR1 COMMANDER LIEUTENANT3
 A A
 TRAITOR2 A A A LIEUTENANT4

 LIEUTENANT1 LIEUTENANT2 LIEUTENANT5

OM(1): Every lieutenant (incl. traitor) acts as commander
 R A
 C L T C
 R R R R R A A A A
 T L T L
 A

 L L L L L L 1
![FTC04_Rollback_Recovery slide 1](images/FTC04_Rollback_Recovery_s001.png)

## Slide 2: Home Exercise: BFT (2/2)  *(visual)*
OM(0): Every lieutenant (incl. traitor) relays the message

 R A
 C L T C
 R R R R A A A
 L T
 A

 L L L L L L

Lieute Value frm Frm Frm Frm Frm Frm Frm Frm Majority
 nant C L1 L2 L3 L4 L5 T1 T2 Vote

 L1 A - A A A A R R A

 L2 A A - A A A R R A

 L3 A A A - A A R R A

 L4 A A A A - A R R A

 L5 A A A A A - R R A

 T1 X X X X X X - X X
 2 T2 X X X X X X X - X
![FTC04_Rollback_Recovery slide 2](images/FTC04_Rollback_Recovery_s002.png)

## Slide 3: Rollback Recovery
(Fault Tolerance in Distributed Systems)

 2110473 Fault Tolerant Computing

## Slide 4: Contents
• Fault Tolerance & Recovery
• Rollback Recovery
• System Model:
 - Messages
 - Consistent State (Cuts)
• Rollback Issues:
 - Domino Effect
 - Livelocks
• Recovery Techniques
 - Coordinated checkpointing
 - Pessimistic Logging

## Slide 5: Fault Tolerance & Recovery  *(visual)*
fault
 causes

 Recovery erroneous state error

 leads to
 valid state
 failure

• An error is a manifestation of a fault that can lead to a failure.
• Failures:
 - Process failure: Deadlocks, protection violation, erroneous user input.
 - System failure: Full/partial amnesia.
 - Secondary storage failure: data inaccessible.
 - Communication failure: network inaccessible.
![FTC04_Rollback_Recovery slide 5](images/FTC04_Rollback_Recovery_s005.png)

## Slide 6: Recovery
Failure of a site/node in a distributed system causes
inconsistencies in the state of the system

Recovery: bringing back the failed node in step with other
nodes in the system
 • Restart process/processor
 • Reclaim resources
 • Undo/finish incomplete transactions
Distributed/Concurrency make things harder

Focus on Message-Passing Model in Distributed Systems

## Slide 7: Failure Recovery
After a failure, restoring the system to its "normal" state
• Forward recovery
 - Assess damages that could be caused by faults, remove
 those damages (errors), and help processes continue
 - TMR is one of Forward recovery
 - Sacrifices cost to achieve availability
• Backward (Rollback) recovery
 - Operation-based (do/undo/redo logs)
 - State-based (Checkpointing/Logging)
 - Sacrifices performance to achieve availability

## Slide 8: System Design Space  *(visual)*
8
![FTC04_Rollback_Recovery slide 8](images/FTC04_Rollback_Recovery_s008.png)

## Slide 9: Forward Recovery
• Repair and go ahead
• Goal: To restore system from erroneous state
 to error-free state
• If nature of error is completely known
 - Remove error from state
 - Proceed with execution from error-free state
• Rarely possible to do

## Slide 10: Forward Recovery (Exception)
◼Exceptions
 −System states that should not occur
 −Exceptions can be defined either
 ◼predefined (e.g. array-index out of bounds, divide by zero)
 ◼explicitly declared by the programmer
◼Raising an exception
 −When such a state is detected in the execution of the
 program
 −The action of indicating occurrence of such as state
◼Exception handler
 −Code to be executed when an exception is raised
 −Declared by the programmer
 −For recovery action
◼Supported by several programming languages
 −Ada, ISO Modula-2, Delphi, Java, C++.

## Slide 11: Backward/Rollback Recovery
• Repairing is not possible so Go back!
• When error source unknown
 - Restore state to previous error-free state; restart
 - Independent of fault, errors causing fault
 - Problems
 • Performance penalty
 • No guarantee fault will not reoccur
 • Possible unrecoverable component of state
• Recovery point: state used to replace error
• Can not be applied to irreversible operations, e.g.
 Print out, ATM withdrawal

## Slide 12: Basic of Rollback Recovery
• Rollback Recovery Protocols
 - Restore the system back to a Consistent State after a failure
 - Achieve Fault Tolerance by periodically saving the state of a process
 during the failure-free execution
 - Treat a distributed system application as a collection of processes that
 communicate over a network
• Checkpoints
 - The Saved States of a process
• Why Rollback Recovery is complicated?
 - Messages induce inter-process dependencies during failure-free
 operation
• Rollback Propagation
 - The dependencies may force some of the processes that did not fail to
 roll back
 - This phenomenon is called "Domino Effect"

## Slide 13: Rollback Recovery
• State based
 - Checkpointing
 • Uncoordinated checkpointing
 • Coordinated checkpointing
 - Blocking, Non-blocking
 • Communication induced checkpointing
 - Model based, Index based
• Log based
 - Pessimisstic logging
 - Optimistic logging
 - Casual logging

## Slide 14: Checkpointing
• Checkpoint recover is the saving and
 restoration of the system state.
• By saving the current state of the system
 periodically, it provides the information
 needed for the restoration of the lost state,
 when the system fails

## Slide 15: Checkpointing issues in
Distributed Environment
• Consistency: if P1 checkpoints and then sends
 a message to P2, we can no longer roll P1 back
 to before the message was sent unless P2 rolls
 back to before the message's receipt
• Expensive: We don't want checkpoint more
 than necessary, but also don't want to have to
 rollback too far
• Communication with the outside world
 doesn't get undone

## Slide 16: System Model  *(visual)*
Basic approaches
 - Checkpointing : copying/restoring the state of a process
 - Logging : recording/replaying messages
![FTC04_Rollback_Recovery slide 16](images/FTC04_Rollback_Recovery_s016.png)

## Slide 17: Stable storage - a prerequisite for recovery
• In a system that tolerates only a single failure,
 stable storage may consist of the volatile
 memory of another process
• In a system that wishes to tolerate an arbitrary
 number of transient failures, stable storage may
 consist of a local disk in each host.
• In a system that tolerates non-transient failures,
 stable storage must consist of a persistent
 medium outside the host on which a process is
 running. A replicated file system is a possible
 implementation in such systems

## Slide 18: Rollback Recovery Principles  *(visual)*
1. Checkpointing
 checkpoint (stored local state)

Inside the cut Outside the cut
 P0

 P1

 P2

 P3

 Recovery line (cut)
 Restart all, or almost all, processes from a consistent cut and
 let a new execution run
![FTC04_Rollback_Recovery slide 18](images/FTC04_Rollback_Recovery_s018.png)

## Slide 19: Rollback Recovery Principles  *(visual)*
2. Message Logging
 checkpoint (stored local state)

 P0

 P1

 P2

 P3

 Only one (or a few) process recover and use message
 information to replay the previous execution until reaching the
 failure point
![FTC04_Rollback_Recovery slide 19](images/FTC04_Rollback_Recovery_s019.png)

## Slide 20: Rollback Recovery Principles  *(visual)*
20
![FTC04_Rollback_Recovery slide 20](images/FTC04_Rollback_Recovery_s020.png)

## Slide 21: Implementation of Rollback Recovery  *(visual)*
On top of a reliable Directly on top of unreliable
 communication protocol communication channels
![FTC04_Rollback_Recovery slide 21](images/FTC04_Rollback_Recovery_s021.png)

## Slide 22: Garbage Collection
• Checkpoints and event logs consume storage
 resources
• Stored Information may become useless for
 Recovery
• Garbage Collection:
 - The deletion of such useless recovery information
 - Common approach is to identify the most recent
 consistent set of checkpoints (Recovery line)
 - And discard all information relating to events that
 occurred before that line

## Slide 23: Messages
• In-transit message
 - messages that have been sent but not yet received
• Lost messages
 - messages whose 'send' is done but 'receive' is undone due to rollback
• Delayed messages
 - messages whose 'receive' is not recorded because the receiving
 process was either down or the message arrived after rollback
• Orphan messages
 - messages with 'receive' recorded but message 'send' not recorded
 - do not arise if processes roll back to a consistent global state
• Duplicate messages
 - arise due to message logging and replaying during process recovery

## Slide 24: In-transit message  *(visual)*
messages that have been sent but not yet received
• If message delivery is not guaranteed, they are not a problem!
• But if the communication protocol is reliable, they must be
 taken into account
![FTC04_Rollback_Recovery slide 24](images/FTC04_Rollback_Recovery_s024.png)

## Slide 25: Lost message  *(visual)*
• Due to the failure in process, the message cound not reach the
 process and so it is lost on the way
• Different from In-transit message

 Rollback
 C1 C2 failure
 P1
 m1
 P2

- Due to the failure in P1, m1 could not reach P1 and lost on the way
- P1 rollback to C2 to recover its old status to continue the task
![FTC04_Rollback_Recovery slide 25](images/FTC04_Rollback_Recovery_s025.png)

## Slide 26: Delayed message  *(visual)*
• The lost messages may reach the destination process after
 recovered, ie. messages arrived after rollback

 Rollback
 m1 reached P1 after
 C0 recovered from failure
 P0
 m5 Rollback
 m5 also delayed
 m1 message C1
 P1
![FTC04_Rollback_Recovery slide 26](images/FTC04_Rollback_Recovery_s026.png)

## Slide 27: Orphan messages  *(visual)*
messages with 'receive' recorded but message 'send' not recorded
• If P2 fails and restarts from the
 cut, the message will be re-
 emitted and received twice by
 P1
 - Either avoid using inconsistent
 cuts (in general for
 checkpointing)
 - Or avoid re-emitting the message
 (in general for message logging)
 and replay the same execution
![FTC04_Rollback_Recovery slide 27](images/FTC04_Rollback_Recovery_s027.png)

## Slide 28: Duplicate message  *(visual)*
• The message which already received has been re-sent after
 recovery

 Rollback

 C1 failure
 P0
 m1

 P1
![FTC04_Rollback_Recovery slide 28](images/FTC04_Rollback_Recovery_s028.png)

## Slide 29: Messages - example  *(visual)*
• In-transit
 - 𝑚1, 𝑚2
• Lost
 - 𝑚1
• Delayed
 - 𝑚1, 𝑚5
• Orphan
 - none
• Duplicated
 - 𝑚4, 𝑚5
![FTC04_Rollback_Recovery slide 29](images/FTC04_Rollback_Recovery_s029.png)

## Slide 30: Consistent State
• A global state of a distributed system
 - a collection of the individual states of all participating processes and the states of
 the communication channels
• Consistent global state
 - a global state that may occur during a failure-free execution of distribution of
 distributed computation
 - if a process's state reflects a message receipt, then the state of the corresponding
 sender must reflect the sending of the message
• A global checkpoint
 - a set of local checkpoints, one from each process
• A consistent global checkpoint
 - a global checkpoint such that no message is sent by a process after taking its local
 point that is received by another process before taking its checkpoint

"A fundamental goal of any rollback-recovery protocol is to
bring the system into a consistent state when
inconsistencies occur because of a failure"

## Slide 31: Consistent/Inconsistent State  *(visual)*
In-transit messages Inconsistent state

 P0

 P1

 P2

 P3

 Consistent State
Orphan message Strongly
 consistent state
![FTC04_Rollback_Recovery slide 31](images/FTC04_Rollback_Recovery_s031.png)

## Slide 32: Domino Effect  *(visual)*
Cascaded rollback which causes the system to roll back to too far
in the computation (even to the beginning), in spite of all the
checkpoints

 failure

 Suppose Y rolls back to y2
 • m is orphan message
 • Process X must rollback to x2
 Suppose Z rolls back to z2
 • Y rolls back to y1
 32 • Force X, Z to roll back to x1, z1
![FTC04_Rollback_Recovery slide 32](images/FTC04_Rollback_Recovery_s032.png)

## Slide 33: Livelocks  *(visual)*
x1
 X n1
 y1 m1
 Y
 failure
 x1
 X n2 n1 y1 m2
 Y
 2nd Rollback

• Y crashes before receiving n1. Y rolls back to Y1 -> X to x1.
• Y recovers, receives n1 and sends m2.
• X recovers, sends n2 but has no record of sending n1
• Hence, Y is forced to rollback second time. X also rolls back as it has
 received m2 but Y has no record of m2.
• Above sequence can repeat indefinitely, causing a livelock.
![FTC04_Rollback_Recovery slide 33](images/FTC04_Rollback_Recovery_s033.png)

## Slide 34: Consistent Checkpoints  *(visual)*
• Overcoming domino effect and livelocks: checkpoints should
 not have messages in transit.
• Consistent checkpoints: no message exchange between any
 pair of processes in the set as well as outside the set during
 the interval spanned by checkpoints.
• {x1,y1,z1} is a strongly consistent checkpoint.

 x1 x2 x3
 X
 m y1 y2
 Y

 Z z1 z2
![FTC04_Rollback_Recovery slide 34](images/FTC04_Rollback_Recovery_s034.png)

## Slide 35: Recovery Techniques  *(visual)*
Rollback-Recovery

 checkpointing logging

uncoordinated coordinated communication pessimistic optimistic causal
 -induced

 blocking non-blocking model-based index-based
![FTC04_Rollback_Recovery slide 35](images/FTC04_Rollback_Recovery_s035.png)

## Slide 36: Techniques that avoid Domino effect
• Coordinated checkpointing rollback recovery
 - processes coordinate their checkpoints to form a system-wide
 consistent state
• Communication-induced checkpointing rollback
 recovery
 - forces each process to take checkpoints based on information
 piggybacked on the application
• Log-based rollback recovery
 - combines checkpointing with logging of non-deterministic events
 - relies on piecewise deterministic (PWD) assumption

## Slide 37: Coordinated/Blocking Protocols  *(visual)*
Rollback-Recovery

 checkpointing x1 x2
 X
 m
 y1 y2
 Y
 coordinated z1 z2
 Z

blocking

 • no messages can be in transit during checkpointing
 • {x1, y1, z1} forms "recovery line"
![FTC04_Rollback_Recovery slide 37](images/FTC04_Rollback_Recovery_s037.png)

## Slide 38: Blocking & Non-blocking Coordinated
Checkpointing
• Blocking Checkpointing
 - After a process takes a local checkpoint, to prevent orphan
 messages, it remains blocked until the entire
 checkpointing activity is complete
 - Disadvantages
 • the computation is blocked during the checkpointing
• Non-blocking Checkpointing
 - The processes need not stop their execution while taking
 checkpoints
 - A fundamental problem in coordinated checkpointing is to
 prevent a process from receiving application messages
 that could make the checkpoint inconsistent.

## Slide 39: Coordinated checkpointing  *(visual)*
• There is an initiator process for the checkpointing
 - Only one (or 2) checkpoint per process (always consistent)
 - large latency: processed blocked until checkpoint is
 finished

 P0: initiator
 checkpoint requests
 P1

 P2

 inconsistency if communications P3
 are not blocked until the end of
 the checkpointing phase
![FTC04_Rollback_Recovery slide 39](images/FTC04_Rollback_Recovery_s039.png)

## Slide 40: Coordinated checkpointing (2)
• Algorithm:
 - block communications while the protocol executes
 - An initiator takes a checkpoint and broadcasts a request
 message to all processes
 - When a process receives this message, it
 • stops its execution,
 • flushes all the communication channels,
 • takes a tentative checkpoint, and
 • sends an acknowledgment message back
 - the coordinator receives acknowledgments from all
 processes, and broadcasts a commit message
 - After receiving the commit each process removes the old
 checkpoint, the new one becomes permanent

## Slide 41: Coordinated Checkpointing (3)  *(visual)*
Overall execution graph
![FTC04_Rollback_Recovery slide 41](images/FTC04_Rollback_Recovery_s041.png)

## Slide 42: Checkpoint inconsistency  *(visual)*
• message m is sent by 𝑃0 after
 receiving a checkpoint request
 from the checkpoint coordinator
 • Assume m reaches 𝑃1 before the
 checkpoint request
 • This situation results in an
 inconsistent checkpoint since
 checkpoint 𝐶1,𝑥shows the
 receipt of message m from 𝑃0,
 while checkpoint 𝐶0,𝑥does not
 show m being sent from 𝑃0
![FTC04_Rollback_Recovery slide 42](images/FTC04_Rollback_Recovery_s042.png)

## Slide 43: Checkpoint inconsistency:  *(visual)*
a solution with FIFO channels

• If channels are FIFO, this
problem can be avoided by
preceding the first post-
checkpoint message on each
channel by a checkpoint request,
forcing each process to take a
checkpoint before receiving the
first post-checkpoint message
![FTC04_Rollback_Recovery slide 43](images/FTC04_Rollback_Recovery_s043.png)

## Slide 44: Uncoordinated checkpointing
• Each process has autonomy in deciding when to take checkpoints
• Advantages
 - The lower runtime overhead during normal execution
• Disadvantages
 - Domino effect during a recovery
 - Recovery from a failure is slow because processes need to iterate to find a
 consistent set of checkpoints
 - Each process maintains multiple checkpoints and periodically invoke a garbage
 collection algorithm
 - Not suitable for application with frequent output commits
• The processes record the dependencies among their checkpoints
 caused by message exchange during failure-free operation

## Slide 45: Communication-induced Checkpointing
• Two types of checkpoints
 - autonomous and forced checkpoints
• Communication-induced checkpointing piggybacks protocol- related
 information on each application message
• The receiver of each application message uses the piggybacked
 information to determine if it has to take a forced checkpoint to
 advance the global recovery line
• The forced checkpoint must be taken before the application may
 process the contents of the message
• In contrast with coordinated checkpointing, no special coordination
 messages are exchanged
• Two types of communication-induced checkpointing
 - model-based checkpointing and index-based checkpointing.

## Slide 46: Log-based Rollback Recovery
• A log-based rollback recovery makes use of deterministic
 and nondeterministic events in a computation.
• Deterministic and Non-deterministic events
 - Non-deterministic events can be the receipt of a message from another
 process or an event internal to the process
 - a message send event is not a non-deterministic event.
 - the execution of process 𝑃0 is a sequence of four deterministic intervals
 - Log-based rollback recovery assumes that all non-deterministic events can
 be identified and their corresponding determinants can be logged into the
 stable storage
 - During failure-free operation, each process logs the determinants of all
 non-deterministic events that it observes onto the stable storage

## Slide 47: Pessimistic Logging
• piecewise determinism = all non-deterministic events can be
 identified and their determinants can be stored on stable
 storage.
• An execution is a sequence of deterministic events (replayed)
 and non-deterministic events (logged and simulated from log)
• determinants of non-deterministic events are stored during
 failure-free execution
• + checkpoints to avoid recovering from the start
• Additional hypothesis: It is possible to prevent a message
 from being sent or received

## Slide 48: Pessimistic Logging
• A process is orphan if it depends on the execution of a non-logged
 non-deterministic event
• Determinant: the information need to "replay" the occurrence of a
 non-deterministic event (e.g., message reception)
• always-no-orphans condition:
 - Stable(e) set of processes with e logged on stable storage
 - Depend(e) set of processes affected by event e
 - Log(e) = set of processes locally storing the event e

else the process is said orphan

## Slide 49: Pessimistic message logging  *(visual)*
• orphan processes are never created but requires a lot of
 synchronizations with the stable storage
• Logs the determinant of ND events before executing them
 synchronous logging (stronger condition)
 Only 1 process
 restarts
 P0

 P1

 P2

 P3
 message resent during recovery
 logged message reception (might have to be cancelled) 49
![FTC04_Rollback_Recovery slide 49](images/FTC04_Rollback_Recovery_s049.png)

## Slide 50: Other Issues
• Output commit
 - the state from which messages are sent to the "outside world"
 can be recovered
 - affects latency of message delivery to "outside world" and
 overhead of checkpoint/logging

• Stable storage
 - survives process failures
 - contains checkpoint/logging information

• Garbage collection
 - removal of checkpoints/logs no longer needed

## Slide 51: HW04: Checkpointing  *(visual)*
▪ Find the consistent cuts in the figure below (passing by ▓)

▪ The recovery line that you found is consistent, strongly consistent or
 inconsistent?
![FTC04_Rollback_Recovery slide 51](images/FTC04_Rollback_Recovery_s051.png)
