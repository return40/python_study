import psutil
#https://psutil.readthedocs.io/en/latest/


#cpu 개수 (물리만)
print('cpu count : ', psutil.cpu_count(logical=False) )
#4

#cpu 개수 (논리포함)
print('cpu count : ', psutil.cpu_count(logical=True) )
#8

#cpu 이용률 (전체)
print(psutil.cpu_percent(interval=1))
#19.0

#cpu 이용률 (각cpu별)
print(psutil.cpu_percent(interval=1, percpu=True))
#[3.1, 3.1, 0.0, 9.4, 3.1, 6.2, 4.7, 0.0]

#메모리 정보
print(psutil.virtual_memory())
#svmem(total=8587886592, available=3588591616, percent=58.2, used=4999294976, free=3588591616)

#스왑 메모리 정보
print(psutil.swap_memory())
#sswap(total=10265608192, used=7354957824, free=2910650368, percent=71.6, sin=0, sout=0)

#디스크 파티션 정보
print(psutil.disk_partitions(all=False))
#[sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='E:\\', mountpoint='E:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='F:\\', mountpoint='F:\\', fstype='', opts='cdrom')]

#디스크 사용량 (경로지정)
print(psutil.disk_usage('C:'))
print(psutil.disk_usage('/'))
#sdiskusage(total=125205606400, used=36909375488, free=88296230912, percent=29.5)

#디스크 I/O
print(psutil.disk_io_counters(perdisk=False, nowrap=False))
#sdiskio(read_count=188988, write_count=112796, read_bytes=4477129728, write_bytes=3053018112, read_time=549, write_time=199)

#네트워크
print(psutil.net_io_counters(pernic=False, nowrap=False))
#snetio(bytes_sent=8890855, bytes_recv=61860753, packets_sent=47020, packets_recv=72003, errin=0, errout=0, dropin=0, dropout=0)


for i in range(1, 11):

    cc = psutil.cpu_percent(interval=1)

    mm = psutil.virtual_memory()

    dd = psutil.disk_usage('C:')

    print('[{:3}] cpu : {:4}% , mem {:4}% , disk {:4}%: '.format(i, cc, mm.percent, dd.percent))

# [  1] cpu : 31.4% , mem 62.7% , disk 29.5%:
# [  2] cpu : 26.9% , mem 62.7% , disk 29.5%:
# [  3] cpu : 28.1% , mem 62.7% , disk 29.5%:
# [  4] cpu : 28.5% , mem 62.7% , disk 29.5%:
# [  5] cpu : 28.1% , mem 62.7% , disk 29.5%:
# [  6] cpu : 27.2% , mem 62.7% , disk 29.5%:
# [  7] cpu : 27.4% , mem 62.7% , disk 29.5%:
# [  8] cpu :  2.1% , mem 62.7% , disk 29.5%:
# [  9] cpu :  3.3% , mem 62.7% , disk 29.5%:
# [ 10] cpu :  5.3% , mem 62.7% , disk 29.5%:

