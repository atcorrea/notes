using System;
using RabbitMQ.Client;
using RabbitMQ.Client.Events;
using System.Text;
using System.Threading;

namespace Worker
{
    class Worker
    {
        static void Main(string[] args)
        {
            var factory = new ConnectionFactory() {HostName = "localhost"};
            using (var connection = factory.CreateConnection())
            {
                using (var channel = connection.CreateModel())
                {
                    channel.QueueDeclare(queue: "task_queue", 
                                        durable: true, //--> persists queue even when rabbitmq dies 
                                        exclusive: false, 
                                        autoDelete: false, 
                                        arguments: null);
                    
                    channel.BasicQos(prefetchSize: 0, prefetchCount: 1, global: false); //each consumer can only process 1 message at a time

                    var consumer = new EventingBasicConsumer(channel);
                    consumer.Received += (model, ea) => {
                        var body = ea.Body.ToArray();
                        var message = Encoding.UTF8.GetString(body);
                        Console.WriteLine($"[X] received: {message}");

                        var dots = message.Split(".").Length -1;
                        Thread.Sleep(dots * 1000);

                        Console.WriteLine("[X] Done");

                        channel.BasicAck(deliveryTag: ea.DeliveryTag, multiple: false);
                    };

                    channel.BasicConsume(queue: "task_queue", 
                                        autoAck: false, //--> ack = acknowledgement (prevents message to be lost before finished beeing processed) 
                                        consumer: consumer);     

                    Console.WriteLine("[*] Waiting for messages. To exit press CTRL+C");
                    Console.ReadKey();               
                }                
            }                        
        }
    }
}
