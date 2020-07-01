using System.Text;
using System;
using RabbitMQ.Client;

namespace Send
{
    //PRODUCER
    class Sender
    {
        public static void Main(string[] args)
        {
            //creating connection:
            var factory = new ConnectionFactory() { HostName = "localhost" };
            using (var connection = factory.CreateConnection())
            {
                using (var channel = connection.CreateModel())
                {
                    //declaring queue
                    channel.QueueDeclare(queue: "hello", durable: false, exclusive: false, autoDelete: false, arguments: null);

                    //generating message
                    var message = "hello";
                    var body = Encoding.UTF8.GetBytes(message);

                    //publishing to queue
                    channel.BasicPublish(exchange: "", routingKey: "hello", basicProperties: null, body: body);

                    Console.WriteLine($"[X] Sent {message}");
                }
            }
            
            Console.WriteLine("Press key to exit");
            Console.ReadKey();
        }

    }
}