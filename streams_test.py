import faust
import logging
from asyncio import sleep

log = logging.getLogger(__name__)


class Plant(faust.Record):
    plant_name: str
    plant_id: int
    type: str
    generation: float


app = faust.App('myapp', broker='kafka://localhost:9092')
source_topic = app.topic('faust_stream_data_12', value_type=Plant)
destination_topic = app.topic('faust_stream_data_13', value_type=Plant)


# specify the source_topic and destination_topic to the agent
@app.agent(source_topic, sink=[destination_topic])
async def hello(messages):
    async for message in messages:
        if message is not None:
            log.info(message.plant_name)
            log.info(message.plant_id)
            log.info(message.type)
            log.info(message.generation)

            message.generation += 1000

            # the yield keyword is used to send the message to the destination_topic
            yield Plant(plant_name=message.plant_name, 
            plant_id=message.plant_id,
            type=message.type,
            generation=message.generation)

            # sleep for 2 seconds
            await sleep(2)
        else:
            log.info('No message received')

if __name__ == '__main__':
    app.main()