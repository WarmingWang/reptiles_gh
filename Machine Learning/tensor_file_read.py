# -*-coding:utf-8 -*-

import tensorflow as tf

with tf.Session() as sess:
    filename=['data/a.jpg', 'data/b.jpg', 'data/c.jpg']
    filename_queue=tf.train.string_input_producer(filename,shuffle=False,num_epochs=5)
    reader=tf.WholeFileReader()
    key,value=reader.read(filename_queue)
    tf.local_variables_initializer().run()
    threads=tf.train.start_queue_runners(sess=sess)

    i=0
    while True:
        i+=1
        image_data=sess.run(value)
        with open('data/read/test_%d.jpg' %i,'wb') as f:
            f.write(image_data)

