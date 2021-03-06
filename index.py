"""
Copyright 2020 Lightbend Inc.
Licensed under the Apache License, Version 2.0.
"""

from akkaserverless.akkaserverless_service import AkkaServerlessService
import logging

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    
    # create service and add components
    service = AkkaServerlessService()
    #service.add_component(entity)
    #service.add_component(view)
    service.start()
