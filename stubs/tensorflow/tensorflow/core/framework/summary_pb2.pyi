"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import sys
import typing

import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import tensorflow.core.framework.tensor_pb2
import tensorflow.tsl.protobuf.histogram_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
from tensorflow.tsl.protobuf.histogram_pb2 import HistogramProto as HistogramProto

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _DataClass:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DataClassEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_DataClass.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DATA_CLASS_UNKNOWN: _DataClass.ValueType  # 0
    """Unknown data class, used (implicitly) for legacy data. Will not be
    processed by data ingestion pipelines.
    """
    DATA_CLASS_SCALAR: _DataClass.ValueType  # 1
    """Scalar time series. Each `Value` for the corresponding tag must have
    `tensor` set to a rank-0 tensor of type `DT_FLOAT` (float32).
    """
    DATA_CLASS_TENSOR: _DataClass.ValueType  # 2
    """Tensor time series. Each `Value` for the corresponding tag must have
    `tensor` set. The tensor value is arbitrary, but should be small to
    accommodate direct storage in database backends: an upper bound of a few
    kilobytes is a reasonable rule of thumb.
    """
    DATA_CLASS_BLOB_SEQUENCE: _DataClass.ValueType  # 3
    """Blob sequence time series. Each `Value` for the corresponding tag must
    have `tensor` set to a rank-1 tensor of bytestring dtype.
    """

class DataClass(_DataClass, metaclass=_DataClassEnumTypeWrapper): ...

DATA_CLASS_UNKNOWN: DataClass.ValueType  # 0
"""Unknown data class, used (implicitly) for legacy data. Will not be
processed by data ingestion pipelines.
"""
DATA_CLASS_SCALAR: DataClass.ValueType  # 1
"""Scalar time series. Each `Value` for the corresponding tag must have
`tensor` set to a rank-0 tensor of type `DT_FLOAT` (float32).
"""
DATA_CLASS_TENSOR: DataClass.ValueType  # 2
"""Tensor time series. Each `Value` for the corresponding tag must have
`tensor` set. The tensor value is arbitrary, but should be small to
accommodate direct storage in database backends: an upper bound of a few
kilobytes is a reasonable rule of thumb.
"""
DATA_CLASS_BLOB_SEQUENCE: DataClass.ValueType  # 3
"""Blob sequence time series. Each `Value` for the corresponding tag must
have `tensor` set to a rank-1 tensor of bytestring dtype.
"""
global___DataClass = DataClass

@typing.final
class SummaryDescription(google.protobuf.message.Message):
    """Metadata associated with a series of Summary data"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TYPE_HINT_FIELD_NUMBER: builtins.int
    type_hint: builtins.str
    """Hint on how plugins should process the data in this series.
    Supported values include "scalar", "histogram", "image", "audio"
    """
    def __init__(
        self,
        *,
        type_hint: builtins.str | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["type_hint", b"type_hint"]) -> None: ...

global___SummaryDescription = SummaryDescription

@typing.final
class SummaryMetadata(google.protobuf.message.Message):
    """A SummaryMetadata encapsulates information on which plugins are able to make
    use of a certain summary value.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class PluginData(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PLUGIN_NAME_FIELD_NUMBER: builtins.int
        CONTENT_FIELD_NUMBER: builtins.int
        plugin_name: builtins.str
        """The name of the plugin this data pertains to."""
        content: builtins.bytes
        """The content to store for the plugin. The best practice is for this to be
        a binary serialized protocol buffer.
        """
        def __init__(
            self,
            *,
            plugin_name: builtins.str | None = ...,
            content: builtins.bytes | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["content", b"content", "plugin_name", b"plugin_name"]) -> None: ...

    PLUGIN_DATA_FIELD_NUMBER: builtins.int
    DISPLAY_NAME_FIELD_NUMBER: builtins.int
    SUMMARY_DESCRIPTION_FIELD_NUMBER: builtins.int
    DATA_CLASS_FIELD_NUMBER: builtins.int
    display_name: builtins.str
    """Display name for viewing in TensorBoard."""
    summary_description: builtins.str
    """Longform readable description of the summary sequence. Markdown supported."""
    data_class: global___DataClass.ValueType
    """Class of data stored in this time series. Required for compatibility with
    TensorBoard's generic data facilities (`DataProvider`, et al.). This value
    imposes constraints on the dtype and shape of the corresponding tensor
    values. See `DataClass` docs for details.
    """
    @property
    def plugin_data(self) -> global___SummaryMetadata.PluginData:
        """Data that associates a summary with a certain plugin."""

    def __init__(
        self,
        *,
        plugin_data: global___SummaryMetadata.PluginData | None = ...,
        display_name: builtins.str | None = ...,
        summary_description: builtins.str | None = ...,
        data_class: global___DataClass.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["plugin_data", b"plugin_data"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["data_class", b"data_class", "display_name", b"display_name", "plugin_data", b"plugin_data", "summary_description", b"summary_description"]) -> None: ...

global___SummaryMetadata = SummaryMetadata

@typing.final
class Summary(google.protobuf.message.Message):
    """A Summary is a set of named values to be displayed by the
    visualizer.

    Summaries are produced regularly during training, as controlled by
    the "summary_interval_secs" attribute of the training operation.
    Summaries are also produced at the end of an evaluation.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class Image(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        HEIGHT_FIELD_NUMBER: builtins.int
        WIDTH_FIELD_NUMBER: builtins.int
        COLORSPACE_FIELD_NUMBER: builtins.int
        ENCODED_IMAGE_STRING_FIELD_NUMBER: builtins.int
        height: builtins.int
        """Dimensions of the image."""
        width: builtins.int
        colorspace: builtins.int
        """Valid colorspace values are
          1 - grayscale
          2 - grayscale + alpha
          3 - RGB
          4 - RGBA
          5 - DIGITAL_YUV
          6 - BGRA
        """
        encoded_image_string: builtins.bytes
        """Image data in encoded format.  All image formats supported by
        image_codec::CoderUtil can be stored here.
        """
        def __init__(
            self,
            *,
            height: builtins.int | None = ...,
            width: builtins.int | None = ...,
            colorspace: builtins.int | None = ...,
            encoded_image_string: builtins.bytes | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["colorspace", b"colorspace", "encoded_image_string", b"encoded_image_string", "height", b"height", "width", b"width"]) -> None: ...

    @typing.final
    class Audio(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        SAMPLE_RATE_FIELD_NUMBER: builtins.int
        NUM_CHANNELS_FIELD_NUMBER: builtins.int
        LENGTH_FRAMES_FIELD_NUMBER: builtins.int
        ENCODED_AUDIO_STRING_FIELD_NUMBER: builtins.int
        CONTENT_TYPE_FIELD_NUMBER: builtins.int
        sample_rate: builtins.float
        """Sample rate of the audio in Hz."""
        num_channels: builtins.int
        """Number of channels of audio."""
        length_frames: builtins.int
        """Length of the audio in frames (samples per channel)."""
        encoded_audio_string: builtins.bytes
        """Encoded audio data and its associated RFC 2045 content type (e.g.
        "audio/wav").
        """
        content_type: builtins.str
        def __init__(
            self,
            *,
            sample_rate: builtins.float | None = ...,
            num_channels: builtins.int | None = ...,
            length_frames: builtins.int | None = ...,
            encoded_audio_string: builtins.bytes | None = ...,
            content_type: builtins.str | None = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["content_type", b"content_type", "encoded_audio_string", b"encoded_audio_string", "length_frames", b"length_frames", "num_channels", b"num_channels", "sample_rate", b"sample_rate"]) -> None: ...

    @typing.final
    class Value(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        NODE_NAME_FIELD_NUMBER: builtins.int
        TAG_FIELD_NUMBER: builtins.int
        METADATA_FIELD_NUMBER: builtins.int
        SIMPLE_VALUE_FIELD_NUMBER: builtins.int
        OBSOLETE_OLD_STYLE_HISTOGRAM_FIELD_NUMBER: builtins.int
        IMAGE_FIELD_NUMBER: builtins.int
        HISTO_FIELD_NUMBER: builtins.int
        AUDIO_FIELD_NUMBER: builtins.int
        TENSOR_FIELD_NUMBER: builtins.int
        node_name: builtins.str
        """This field is deprecated and will not be set."""
        tag: builtins.str
        """Tag name for the data. Used by TensorBoard plugins to organize data. Tags
        are often organized by scope (which contains slashes to convey
        hierarchy). For example: foo/bar/0
        """
        simple_value: builtins.float
        obsolete_old_style_histogram: builtins.bytes
        @property
        def metadata(self) -> global___SummaryMetadata:
            """Contains metadata on the summary value such as which plugins may use it.
            Take note that many summary values may lack a metadata field. This is
            because the FileWriter only keeps a metadata object on the first summary
            value with a certain tag for each tag. TensorBoard then remembers which
            tags are associated with which plugins. This saves space.
            """

        @property
        def image(self) -> global___Summary.Image: ...
        @property
        def histo(self) -> tensorflow.tsl.protobuf.histogram_pb2.HistogramProto: ...
        @property
        def audio(self) -> global___Summary.Audio: ...
        @property
        def tensor(self) -> tensorflow.core.framework.tensor_pb2.TensorProto: ...
        def __init__(
            self,
            *,
            node_name: builtins.str | None = ...,
            tag: builtins.str | None = ...,
            metadata: global___SummaryMetadata | None = ...,
            simple_value: builtins.float | None = ...,
            obsolete_old_style_histogram: builtins.bytes | None = ...,
            image: global___Summary.Image | None = ...,
            histo: tensorflow.tsl.protobuf.histogram_pb2.HistogramProto | None = ...,
            audio: global___Summary.Audio | None = ...,
            tensor: tensorflow.core.framework.tensor_pb2.TensorProto | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["audio", b"audio", "histo", b"histo", "image", b"image", "metadata", b"metadata", "obsolete_old_style_histogram", b"obsolete_old_style_histogram", "simple_value", b"simple_value", "tensor", b"tensor", "value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["audio", b"audio", "histo", b"histo", "image", b"image", "metadata", b"metadata", "node_name", b"node_name", "obsolete_old_style_histogram", b"obsolete_old_style_histogram", "simple_value", b"simple_value", "tag", b"tag", "tensor", b"tensor", "value", b"value"]) -> None: ...
        def WhichOneof(self, oneof_group: typing.Literal["value", b"value"]) -> typing.Literal["simple_value", "obsolete_old_style_histogram", "image", "histo", "audio", "tensor"] | None: ...

    VALUE_FIELD_NUMBER: builtins.int
    @property
    def value(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Summary.Value]:
        """Set of values for the summary."""

    def __init__(
        self,
        *,
        value: collections.abc.Iterable[global___Summary.Value] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["value", b"value"]) -> None: ...

global___Summary = Summary
