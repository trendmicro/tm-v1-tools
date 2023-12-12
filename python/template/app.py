import logging

import requests

import pytmv1
from pytmv1 import (
    AccountTask,
    AccountTaskResp,
    CollectFileTaskResp,
    EmailMessageIdTask,
    EmailMessageTaskResp,
    EmailMessageUIdTask,
    EndpointTask,
    EndpointTaskResp,
    FileTask,
    InvestigationStatus,
    ObjectTask,
    ObjectType,
    ProcessTask,
    QueryOp,
    ResultCode,
    ScanAction,
    SuspiciousObjectTask,
)

APP_NAME = "myAppName"
V1_API_TOKEN = "vision_one_api_token"
V1_API_URL = "https://vision_one_api_url.com"

logging.basicConfig(level=logging.DEBUG)

client = pytmv1.client(APP_NAME, V1_API_TOKEN, V1_API_URL)


def is_success(result):
    return result.result_code == ResultCode.SUCCESS


def check_connectivity():
    result = client.check_connectivity()
    if is_success(result):
        if result.response.status == "available":
            print("The API service is available")
    else:
        print(result.error)


def disable_account():
    result = client.disable_account(
        AccountTask(accountName="ghost@trendmicro.com"),
        AccountTask(accountName="ghost2@trendmicro.com"),
    )
    for item in result.response.items:
        task_result = client.get_task_result(item.task_id, AccountTaskResp)
        print(task_result.response.status)


def enable_account():
    result = client.enable_account(
        AccountTask(accountName="ghost@trendmicro.com"),
        AccountTask(accountName="ghost2@trendmicro.com"),
    )
    for item in result.response.items:
        task_result = client.get_task_result(item.task_id, AccountTaskResp)
        print(task_result.response.status)


def reset_password_account():
    result = client.reset_password_account(
        AccountTask(accountName="ghost@trendmicro.com"),
        AccountTask(accountName="ghost2@trendmicro.com"),
    )
    for item in result.response.items:
        task_result = client.get_task_result(item.task_id, AccountTaskResp)
        print(task_result.response.status)


def sign_out_account():
    result = client.sign_out_account(
        AccountTask(accountName="ghost@trendmicro.com"),
        AccountTask(accountName="ghost2@trendmicro.com"),
    )
    for item in result.response.items:
        task_result = client.get_task_result(item.task_id, AccountTaskResp)
        print(task_result.response.status)


def delete_email_message():
    result = client.delete_email_message(
        EmailMessageIdTask(messageId="1"), EmailMessageUIdTask(uniqueId="2")
    )
    for item in result.response.items:
        task_result = client.get_task_result(
            item.task_id, EmailMessageTaskResp
        )
        print(task_result.response.status)


def quarantine_email_message():
    result = client.quarantine_email_message(
        EmailMessageIdTask(messageId="1"), EmailMessageUIdTask(uniqueId="2")
    )
    for item in result.response.items:
        task_result = client.get_task_result(
            item.task_id, EmailMessageTaskResp
        )
        print(task_result.response.status)


def restore_email_message():
    result = client.restore_email_message(
        EmailMessageIdTask(messageId="1"), EmailMessageUIdTask(uniqueId="2")
    )
    for item in result.response.items:
        task_result = client.get_task_result(
            item.task_id, EmailMessageTaskResp
        )
        print(task_result.response.status)


def collect_file():
    result = client.collect_file(
        FileTask(
            endpointName="endpoint1", filePath="/tmp/to_be_collected1.txt"
        ),
        FileTask(
            endpointName="endpoint2", filePath="/tmp/to_be_collected2.txt"
        ),
    )
    for item in result.response.items:
        task_result = client.get_task_result(item.task_id, CollectFileTaskResp)
        print(task_result.response.resource_location)


def isolate_endpoint():
    result = client.isolate_endpoint(
        EndpointTask(endpointName="endpoint1"),
        EndpointTask(endpointName="endpoint2"),
    )
    for item in result.response.items:
        task_result = client.get_task_result(item.task_id, EndpointTaskResp)
        print(task_result.response.status)


def restore_endpoint():
    result = client.restore_endpoint(
        EndpointTask(endpointName="endpoint1"),
        EndpointTask(endpointName="endpoint2"),
    )
    for item in result.response.items:
        task_result = client.get_task_result(item.task_id, EndpointTaskResp)
        print(task_result.response.status)


def terminate_process():
    result = client.terminate_process(
        ProcessTask(
            endpointName="endpoint1",
            fileSha1="da39a3ee5e6b4b0d3255bfef95601890afd80709",
        ),
        ProcessTask(endpointName="endpoint2"),
    )
    for item in result.response.items:
        task_result = client.get_task_result(item.task_id, EndpointTaskResp)
        print(task_result.response.status)


def add_to_block_list():
    result = client.add_to_block_list(
        ObjectTask(objectType=ObjectType.IP, objectValue="1.1.1.1"),
        ObjectTask(
            objectType=ObjectType.DOMAIN, objectValue="dummydomain.com"
        ),
    )
    for item in result.response.items:
        print(item.task_id)
        print(item.status)


def add_to_exception_list():
    result = client.add_to_exception_list(
        ObjectTask(objectType=ObjectType.IP, objectValue="1.1.1.1"),
        ObjectTask(
            objectType=ObjectType.DOMAIN, objectValue="dummydomain.com"
        ),
    )
    for item in result.response.items:
        print(item.task_id)
        print(item.status)


def add_to_suspicious_list():
    result = client.add_to_suspicious_list(
        SuspiciousObjectTask(
            objectType=ObjectType.IP,
            objectValue="1.1.1.1",
            scanAction=ScanAction.BLOCK,
        )
    )
    for item in result.response.items:
        print(item.task_id)
        print(item.status)


def get_exception_list():
    result = client.get_exception_list()
    for item in result.response.items:
        print(item.value)
        print(item.type)
        print(item.description)


def get_suspicious_list():
    result = client.get_suspicious_list()
    for item in result.response.items:
        print(item.value)
        print(item.type)
        print(item.risk_level)


def remove_from_exception_list():
    result = client.remove_from_exception_list(
        ObjectTask(objectType=ObjectType.IP, objectValue="1.1.1.1"),
        ObjectTask(
            objectType=ObjectType.URL, objectValue="https://dummyurl.com"
        ),
    )
    for item in result.response.items:
        print(item.task_id)
        print(item.status)


def remove_from_suspicious_list():
    result = client.remove_from_suspicious_list(
        ObjectTask(objectType=ObjectType.IP, objectValue="1.1.1.1"),
        ObjectTask(
            objectType=ObjectType.URL, objectValue="https://dummyurl.com"
        ),
    )
    for item in result.response.items:
        print(item.task_id)
        print(item.status)


def download_sandbox_analysis_result():
    result = client.download_sandbox_analysis_result("12345")
    with open("analysis_result.pdf", "wb") as binary_file:
        binary_file.write(result.response.content)


def download_sandbox_investigation_package():
    result = client.download_sandbox_investigation_package("12345")
    with open("investigation_package.zip", "wb") as binary_file:
        binary_file.write(result.response.content)


def get_sandbox_analysis_result():
    result = client.get_sandbox_analysis_result("12345")
    print(result.response.analysis_completion_date_time)
    print(result.response.id)
    print(result.response.type)
    print(result.response.risk_level)


def get_sandbox_submission_status():
    result = client.get_sandbox_submission_status("12345")
    print(result.response.status)
    print(result.response.resource_location)


def get_sandbox_suspicious_list():
    result = client.get_sandbox_suspicious_list("12345")
    for item in result.response.items:
        print(item.analysis_completion_date_time)
        print(item.value)
        print(item.type)
        print(item.risk_level)


def submit_file_to_sandbox():
    file = requests.get(
        "https://www.dummyurl.com/dummyfile.zip", allow_redirects=True
    )
    client.submit_file_to_sandbox(file.content, "dummyfile.zip")


def submit_urls_to_sandbox():
    client.submit_urls_to_sandbox(
        "https://dummyurl.com", "https://dummyurl.com2/"
    )


def get_email_activity_data():
    result = client.get_email_activity_data(
        mailMsgSubject="spam", mailSenderIp="192.169.1.1"
    )
    for item in result.response.items:
        print(item.event_time)
        print(item.mail_from_addresses)
        print(item.mail_msg_id)
        print(item.mail_msg_subject)


def get_email_activity_data_count():
    result = client.get_email_activity_data_count(mailMsgSubject="spam")
    print(result.response.total_count)


def get_endpoint_activity_data():
    result = client.get_endpoint_activity_data(dpt="443")
    for item in result.response.items:
        print(item.request)
        print(item.dpt)
        print(item.endpoint_ip)


def get_endpoint_activity_count():
    result = client.get_endpoint_activity_data_count(dpt="443")
    print(result.response.total_count)


def get_endpoint_data():
    result = client.get_endpoint_data(QueryOp.AND, "client1")
    for item in result.response.items:
        print(item.ip)
        print(item.endpoint_name)
        print(item.agent_guid)


def add_alert_note():
    result = client.add_alert_note("1", "dummy note")
    print(result.response.note_id())
    print(result.response.location)


def consume_alert_list():
    result_list = []
    result = client.consume_alert_list(
        lambda alert: result_list.append(alert),
        "2020-06-15T10:00:00Z",
        "2020-06-15T10:00:00Z",
    )
    print(result.response.total_consumed)
    print(result_list)


def get_alert_list():
    result = client.get_alert_list(
        "2020-06-15T10:00:00Z", "2020-06-15T10:00:00Z"
    )
    for item in result.response.items:
        print(item.description)
        print(item.id)
        print(item.model)
        print(item.impact_scope)


def get_alert_details():
    result = client.get_alert_details("WB-12345")
    print(result.response.alert)
    print(result.response.etag)


def edit_alert_status():
    result = client.edit_alert_status(
        "1",
        InvestigationStatus.IN_PROGRESS,
        "d41d8cd98f00b204e9800998ecf8427e",
    )
    print(result.result_code)
