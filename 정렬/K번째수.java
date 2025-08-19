import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        
        for(int i=0; i<commands.length; i++) {
            // i번째 command에 대해 부분 배열을 생성
            int[] temp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            // 📌Arrays.copyOfRange(): 지정한 배열에서 특정 범위만큼의 요소들을 복사해 새로운 배열로 반환하는 메서드 
            // 예를 들어, CopyOfRange(Single[], Int32, Int32)는 지정된 배열의 지정된 범위를 새 배열에 복사
            
            // 💡인덱스 번호는 0번부터 시작하지만, 문제에서는 1번부터 번호를 매기기 때문에
            // 인덱스 번호 1번(j) 값에 -1을 해줘야 함!!
            
            Arrays.sort(temp); // 생성한 부분 배열을 오름차순 정렬
            // 정렬된 배열에서 i번째 숫자를 추출하여 answer 배열에 저장
            
            answer[i] = temp[commands[i][2]-1];
            // 마찬가지로, 만약 i가 2면 temp[commands[2][2]]
            // temp[commands[3]] 인덱스 범위를 벗어나므로 -1을 해야함
        }
        
        return answer;
    }
}
