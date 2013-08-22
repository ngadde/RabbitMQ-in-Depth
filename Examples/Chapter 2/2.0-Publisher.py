import rmqid

url = 'amqp://guest:guest@localhost:5672/%2F'

# Connect to RabbitMQ using the URL above
connection = rmqid.Connection(url)

# Open a new channel on the connection
channel = connection.channel()

# Create a new exchange object, passing in the channel to use
exchange = rmqid.Exchange(channel, 'chapter2-example')

# Declare the exchange on the RabbitMQ server
exchange.declare()

# Create a new queue object, passing in the channel to use
queue = rmqid.Queue(channel, 'example')

# Declare the queue on the RabbitMQ server
queue.declare()

# Bind the queue to the exchange on the RabbitMQ server
queue.bind(exchange, 'example-routing-key')

for message_number in range(0, 10):
    message = rmqid.Message(channel,
                           'Test message #%i' % message_number,
                           {'content_type': 'text/plain'})
    message.publish(exchange, 'example-routing-key')
