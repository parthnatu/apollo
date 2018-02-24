// Generated by gencpp from file speech_service/ReturnDetectedSpeechRequest.msg
// DO NOT EDIT!


#ifndef SPEECH_SERVICE_MESSAGE_RETURNDETECTEDSPEECHREQUEST_H
#define SPEECH_SERVICE_MESSAGE_RETURNDETECTEDSPEECHREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace speech_service
{
template <class ContainerAllocator>
struct ReturnDetectedSpeechRequest_
{
  typedef ReturnDetectedSpeechRequest_<ContainerAllocator> Type;

  ReturnDetectedSpeechRequest_()
    {
    }
  ReturnDetectedSpeechRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }






  typedef boost::shared_ptr< ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> const> ConstPtr;

}; // struct ReturnDetectedSpeechRequest_

typedef ::speech_service::ReturnDetectedSpeechRequest_<std::allocator<void> > ReturnDetectedSpeechRequest;

typedef boost::shared_ptr< ::speech_service::ReturnDetectedSpeechRequest > ReturnDetectedSpeechRequestPtr;
typedef boost::shared_ptr< ::speech_service::ReturnDetectedSpeechRequest const> ReturnDetectedSpeechRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace speech_service

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "speech_service/ReturnDetectedSpeechRequest";
  }

  static const char* value(const ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
";
  }

  static const char* value(const ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ReturnDetectedSpeechRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::speech_service::ReturnDetectedSpeechRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // SPEECH_SERVICE_MESSAGE_RETURNDETECTEDSPEECHREQUEST_H
