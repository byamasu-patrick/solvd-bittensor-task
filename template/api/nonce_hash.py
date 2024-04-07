
import bittensor as bt
from typing import List, Optional, Union, Any, Dict
from template.protocol import Dummy
from bittensor.subnets import SubnetsAPI


class NonceHashAPI(SubnetsAPI):
    def __init__(self, wallet: "bt.wallet"):
        super().__init__(wallet)
        self.netuid = 33
        self.name = "dummy"
        self.synapse = bt.Synapse()

    def prepare_synapse(self, dummy_input: int) -> Dummy:
        synapse.dummy_input = dummy_input

        return synapse

    def process_responses(
        self, responses: List[Union["bt.Synapse", Any]]
    ) -> List[int]:
        outputs = []
        success = False
        failure_modes = {"code": [], "message": []}
        for response in responses:
            if response.dendrite.status_code != 200:
                failure_modes["code"].append(response.dendrite.status_code)
                failure_modes["message"].append(
                    response.dendrite.status_message
                )                
                continue

            store_id = (
                response.data_hash.decode("utf-8")
                if isinstance(response.data_has, bytes)
                else response.data_hash
            )

            bt.logging.debug(f"receive data CID: {store_id}")
            success = True

            return outputs.append(response.dummy_output)
        return outputs
