using System.Text;
using System;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;

namespace Receive
{
    //CONSUMER
    class Receiver
    {
        static void Main(string[] args)
        {
            //opening connection
            var factory = new ConnectionFactory() {HostName = "localhost"};
            using (var connection = factory.CreateConnection())
            {
                using (var channel = connection.CreateModel())
                {
                    //declaring queue
                    channel.QueueDeclare(queue: "hello", durable: false, exclusive: false, autoDelete: false, arguments: null);

                    //creating handler for message received
                    var consumer = new EventingBasicConsumer(channel);
                    consumer.Received += (model, ea) => {
                        var body = ea.Body.ToArray();
                        var message = Encoding.UTF8.GetString(body);
                        Console.WriteLine($"[X] received {message}");
                    };

                    //consuming messages (handler adding)
                    channel.BasicConsume(queue: "hello", autoAck: true, consumer: consumer);     

                    Console.WriteLine("Press a key to exit");
                    Console.ReadKey();               
                }                
            }                        
        }
    }
}
