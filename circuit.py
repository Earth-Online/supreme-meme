from collections import deque

class TimeSegment:
    def __init__(self,time,action):
        self.__time = time
        self.__actions = deque()
        self.__actions.append(action)
    def time(self):
        return self.__time
    def actions(self):
        return self.__actions

class Agenda:
    def __init__(self):
        self.__current_time = 0
        self.__segments = []
    def empty(self):
        return len(self.__segments) == 0
    def current_time(self):
        return self.__current_time
    def set_current_time(self,time):
        self.__current_time = time
    def segments(self):
        return self.__segments
    def first_segment_item(self):
        self.__current_time = self.__segments[0].time()
        return self.__segments[0].actions()[0]
    def remove_first_segment_item(self):
        actions = self.segments()[0].actions()
        actions.popleft()
        if len(actions) == 0:
            self.segments().pop(0)
    def add_to_agenda(self,time,action):
        insert_index = 0
        for i in range(len(self.segments())):
            if time == self.segments()[i].time():
                self.segments()[i].actions().append(action)
                insert_index = -1
                break
            elif time > self.segments()[i].time():
                insert_index = i + 1
        if insert_index != -1:
            self.segments().insert(insert_index,TimeSegment(time,action))
                
agenda = Agenda()

def progagate():
    if agenda.empty():
        return
    agenda.first_segment_item()()
    agenda.remove_first_segment_item()
    progagate()
def after_delay(delay_time,action):
    agenda.add_to_agenda(delay_time + agenda.current_time(),action)

class Wire:
    def __init__(self):
        self.__signal = 0
        self.__actions = []
    def signal(self):
        return self.__signal
    def set_signal(self,signal):
        self.__signal = signal
        for action in self.actions():
            action()
    def actions(self):
        return self.__actions
    def add_action(self,action):
        self.__actions.insert(0,action)

invert_gate_delay = 2
and_gate_delay = 3
or_gate_delay = 5

def invert_gate(input_wire,output_wire):
    def invert_action():
        new_value = input_wire.signal() == 0 and 1 or 0
        after_delay(invert_gate_delay,
                    lambda : output_wire.set_signal(new_value))
    action = invert_action
    input_wire.add_action(action)

def and_gate(input_wire_1,input_wire_2,output_wire):
    def and_action():
        new_value = input_wire_1.signal() == input_wire_2.signal() and input_wire_1.signal() == 1 and 1 or 0
        after_delay(and_gate_delay,
                    lambda : output_wire.set_signal(new_value))
    action = and_action
    input_wire_1.add_action(action)
    input_wire_2.add_action(action)

def or_gate(input_wire_1,input_wire_2,output_wire):
    def or_action():
        new_value = input_wire_1.signal() == input_wire_2.signal() and input_wire_1.signal() == 0 and 0 or 1
        after_delay(or_gate_delay,
                    lambda : output_wire.set_signal(new_value))
    action = or_action
    input_wire_1.add_action(action)
    input_wire_2.add_action(action)


def half_adder(a,b,s,c):
    d = Wire()
    e = Wire()
    or_gate(a,b,d)
    and_gate(a,b,c)
    invert_gate(c,e)
    and_gate(d,e,s)

def full_adder(a,b,c_in,sum_value,c_out):
    s,c1,c2 = Wire(),Wire(),Wire()
    half_adder(b,c_in,s,c1)
    half_adder(a,s,sum_value,c2)
    or_gate(c1,c2,c_out)

a = Wire()
b = Wire()
c = Wire()
d = Wire()
e = Wire()
s = Wire()

half_adder(a,b,s,c)
a.set_signal(1)
progagate()
print(s.signal()) # 1
print(c.signal()) # 0

b.set_signal(1)
progagate()
print(s.signal()) # 0
print(c.signal()) # 1
