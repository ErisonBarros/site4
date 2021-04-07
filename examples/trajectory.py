#
# This file is part of Python Client Library for WLTS.
# Copyright (C) 2020-2021 INPE.
#
# Python Client Library for WLTS is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""WLTS Python Client Examples."""
from wlts import WLTS

# Specify the URL of the WLTS instance to be used
service = WLTS('https://brazildatacube.dpi.inpe.br/wlts/')

tj = service.tj(latitude=[-12.0, -10.3378], longitude=[-47.3200, -54.0], start_date='2010')
print(tj)


# Example of trajectory operation
tj = service.tj(latitude=-12.0, longitude=-54.0)

print(tj[0].trajectory)

# The collection name may not be same.
# Make sure the collection is available in service
tj_two = service.tj(latitude=-10.3378, longitude=-47.3200, collections='prodes_cerrado', geometry=True)

print(tj_two[0].trajectory)