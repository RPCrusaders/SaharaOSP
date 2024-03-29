# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import marketplace_pb2 as marketplace__pb2


class MarketplaceStub(object):
    """
    SellItem should make the seller stream for notifications on that product,
    and that notification is basically sent through BuyItem.
    In a similar vein we have AddToWishList that should make buyers stream for notifications
    on that product, notifications being sent on a UpdateItem call by a seller.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterSeller = channel.unary_unary(
                '/Marketplace/RegisterSeller',
                request_serializer=marketplace__pb2.RegisterSellerRequest.SerializeToString,
                response_deserializer=marketplace__pb2.RegisterSellerResponse.FromString,
                )
        self.DeleteItem = channel.unary_unary(
                '/Marketplace/DeleteItem',
                request_serializer=marketplace__pb2.DeleteItemRequest.SerializeToString,
                response_deserializer=marketplace__pb2.DeleteItemResponse.FromString,
                )
        self.DisplaySellerItems = channel.unary_unary(
                '/Marketplace/DisplaySellerItems',
                request_serializer=marketplace__pb2.DisplaySellerItemsRequest.SerializeToString,
                response_deserializer=marketplace__pb2.DisplaySellerItemsResponse.FromString,
                )
        self.SellItem = channel.unary_unary(
                '/Marketplace/SellItem',
                request_serializer=marketplace__pb2.SellItemRequest.SerializeToString,
                response_deserializer=marketplace__pb2.SellItemResponse.FromString,
                )
        self.SearchItem = channel.unary_unary(
                '/Marketplace/SearchItem',
                request_serializer=marketplace__pb2.SearchItemRequest.SerializeToString,
                response_deserializer=marketplace__pb2.SearchItemResponse.FromString,
                )
        self.RateItem = channel.unary_unary(
                '/Marketplace/RateItem',
                request_serializer=marketplace__pb2.RateItemRequest.SerializeToString,
                response_deserializer=marketplace__pb2.RateItemResponse.FromString,
                )
        self.WishlistItem = channel.unary_unary(
                '/Marketplace/WishlistItem',
                request_serializer=marketplace__pb2.WishlistRequest.SerializeToString,
                response_deserializer=marketplace__pb2.WishlistResponse.FromString,
                )
        self.UpdateItem = channel.unary_unary(
                '/Marketplace/UpdateItem',
                request_serializer=marketplace__pb2.UpdateItemRequest.SerializeToString,
                response_deserializer=marketplace__pb2.UpdateItemResponse.FromString,
                )
        self.BuyItem = channel.unary_unary(
                '/Marketplace/BuyItem',
                request_serializer=marketplace__pb2.BuyItemRequest.SerializeToString,
                response_deserializer=marketplace__pb2.BuyItemResponse.FromString,
                )


class MarketplaceServicer(object):
    """
    SellItem should make the seller stream for notifications on that product,
    and that notification is basically sent through BuyItem.
    In a similar vein we have AddToWishList that should make buyers stream for notifications
    on that product, notifications being sent on a UpdateItem call by a seller.

    """

    def RegisterSeller(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisplaySellerItems(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SellItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RateItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WishlistItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BuyItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MarketplaceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterSeller': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterSeller,
                    request_deserializer=marketplace__pb2.RegisterSellerRequest.FromString,
                    response_serializer=marketplace__pb2.RegisterSellerResponse.SerializeToString,
            ),
            'DeleteItem': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteItem,
                    request_deserializer=marketplace__pb2.DeleteItemRequest.FromString,
                    response_serializer=marketplace__pb2.DeleteItemResponse.SerializeToString,
            ),
            'DisplaySellerItems': grpc.unary_unary_rpc_method_handler(
                    servicer.DisplaySellerItems,
                    request_deserializer=marketplace__pb2.DisplaySellerItemsRequest.FromString,
                    response_serializer=marketplace__pb2.DisplaySellerItemsResponse.SerializeToString,
            ),
            'SellItem': grpc.unary_unary_rpc_method_handler(
                    servicer.SellItem,
                    request_deserializer=marketplace__pb2.SellItemRequest.FromString,
                    response_serializer=marketplace__pb2.SellItemResponse.SerializeToString,
            ),
            'SearchItem': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchItem,
                    request_deserializer=marketplace__pb2.SearchItemRequest.FromString,
                    response_serializer=marketplace__pb2.SearchItemResponse.SerializeToString,
            ),
            'RateItem': grpc.unary_unary_rpc_method_handler(
                    servicer.RateItem,
                    request_deserializer=marketplace__pb2.RateItemRequest.FromString,
                    response_serializer=marketplace__pb2.RateItemResponse.SerializeToString,
            ),
            'WishlistItem': grpc.unary_unary_rpc_method_handler(
                    servicer.WishlistItem,
                    request_deserializer=marketplace__pb2.WishlistRequest.FromString,
                    response_serializer=marketplace__pb2.WishlistResponse.SerializeToString,
            ),
            'UpdateItem': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateItem,
                    request_deserializer=marketplace__pb2.UpdateItemRequest.FromString,
                    response_serializer=marketplace__pb2.UpdateItemResponse.SerializeToString,
            ),
            'BuyItem': grpc.unary_unary_rpc_method_handler(
                    servicer.BuyItem,
                    request_deserializer=marketplace__pb2.BuyItemRequest.FromString,
                    response_serializer=marketplace__pb2.BuyItemResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Marketplace', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Marketplace(object):
    """
    SellItem should make the seller stream for notifications on that product,
    and that notification is basically sent through BuyItem.
    In a similar vein we have AddToWishList that should make buyers stream for notifications
    on that product, notifications being sent on a UpdateItem call by a seller.

    """

    @staticmethod
    def RegisterSeller(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Marketplace/RegisterSeller',
            marketplace__pb2.RegisterSellerRequest.SerializeToString,
            marketplace__pb2.RegisterSellerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Marketplace/DeleteItem',
            marketplace__pb2.DeleteItemRequest.SerializeToString,
            marketplace__pb2.DeleteItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisplaySellerItems(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Marketplace/DisplaySellerItems',
            marketplace__pb2.DisplaySellerItemsRequest.SerializeToString,
            marketplace__pb2.DisplaySellerItemsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SellItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Marketplace/SellItem',
            marketplace__pb2.SellItemRequest.SerializeToString,
            marketplace__pb2.SellItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Marketplace/SearchItem',
            marketplace__pb2.SearchItemRequest.SerializeToString,
            marketplace__pb2.SearchItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RateItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Marketplace/RateItem',
            marketplace__pb2.RateItemRequest.SerializeToString,
            marketplace__pb2.RateItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WishlistItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Marketplace/WishlistItem',
            marketplace__pb2.WishlistRequest.SerializeToString,
            marketplace__pb2.WishlistResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Marketplace/UpdateItem',
            marketplace__pb2.UpdateItemRequest.SerializeToString,
            marketplace__pb2.UpdateItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def BuyItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Marketplace/BuyItem',
            marketplace__pb2.BuyItemRequest.SerializeToString,
            marketplace__pb2.BuyItemResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class notificationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendNotification = channel.unary_unary(
                '/notification/SendNotification',
                request_serializer=marketplace__pb2.NotificationRequest.SerializeToString,
                response_deserializer=marketplace__pb2.NotificationResponse.FromString,
                )


class notificationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendNotification(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_notificationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendNotification': grpc.unary_unary_rpc_method_handler(
                    servicer.SendNotification,
                    request_deserializer=marketplace__pb2.NotificationRequest.FromString,
                    response_serializer=marketplace__pb2.NotificationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'notification', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class notification(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendNotification(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/notification/SendNotification',
            marketplace__pb2.NotificationRequest.SerializeToString,
            marketplace__pb2.NotificationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
