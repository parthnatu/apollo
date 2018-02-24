// Generated by gencpp from file speech_service/ReturnDetectedSpeech.msg
// DO NOT EDIT!


#ifndef SPEECH_SERVICE_MESSAGE_RETURNDETECTEDSPEECH_H
#define SPEECH_SERVICE_MESSAGE_RETURNDETECTEDSPEECH_H

#include <ros/service_traits.h>


#include <speech_service/ReturnDetectedSpeechRequest.h>
#include <speech_service/ReturnDetectedSpeechResponse.h>


namespace speech_service
{

struct ReturnDetectedSpeech
{

typedef ReturnDetectedSpeechRequest Request;
typedef ReturnDetectedSpeechResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct ReturnDetectedSpeech
} // namespace speech_service


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::speech_service::ReturnDetectedSpeech > {
  static const char* value()
  {
    return "74697ed3d931f6eede8bf3a8dfeca160";
  }

  static const char* value(const ::speech_service::ReturnDetectedSpeech&) { return value(); }
};

template<>
struct DataType< ::speech_service::ReturnDetectedSpeech > {
  static const char* value()
  {
    return "speech_service/ReturnDetectedSpeech";
  }

  static const char* value(const ::speech_service::ReturnDetectedSpeech&) { return value(); }
};


// service_traits::MD5Sum< ::speech_service::ReturnDetectedSpeechRequest> should match 
// service_traits::MD5Sum< ::speech_service::ReturnDetectedSpeech > 
template<>
struct MD5Sum< ::speech_service::ReturnDetectedSpeechRequest>
{
  static const char* value()
  {
    return MD5Sum< ::speech_service::ReturnDetectedSpeech >::value();
  }
  static const char* value(const ::speech_service::ReturnDetectedSpeechRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::speech_service::ReturnDetectedSpeechRequest> should match 
// service_traits::DataType< ::speech_service::ReturnDetectedSpeech > 
template<>
struct DataType< ::speech_service::ReturnDetectedSpeechRequest>
{
  static const char* value()
  {
    return DataType< ::speech_service::ReturnDetectedSpeech >::value();
  }
  static const char* value(const ::speech_service::ReturnDetectedSpeechRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::speech_service::ReturnDetectedSpeechResponse> should match 
// service_traits::MD5Sum< ::speech_service::ReturnDetectedSpeech > 
template<>
struct MD5Sum< ::speech_service::ReturnDetectedSpeechResponse>
{
  static const char* value()
  {
    return MD5Sum< ::speech_service::ReturnDetectedSpeech >::value();
  }
  static const char* value(const ::speech_service::ReturnDetectedSpeechResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::speech_service::ReturnDetectedSpeechResponse> should match 
// service_traits::DataType< ::speech_service::ReturnDetectedSpeech > 
template<>
struct DataType< ::speech_service::ReturnDetectedSpeechResponse>
{
  static const char* value()
  {
    return DataType< ::speech_service::ReturnDetectedSpeech >::value();
  }
  static const char* value(const ::speech_service::ReturnDetectedSpeechResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // SPEECH_SERVICE_MESSAGE_RETURNDETECTEDSPEECH_H
