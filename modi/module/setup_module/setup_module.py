from modi.module.module import Module


class SetupModule(Module):
    def __init__(self, id_, uuid, msg_send_q):
        super(SetupModule, self).__init__(id_, uuid, msg_send_q)
